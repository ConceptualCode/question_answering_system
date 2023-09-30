# Author: Anthony Soronnadi

import os
import csv
import json
import requests
from requests.auth import HTTPBasicAuth
from elasticsearch import Elasticsearch
from config import ELASTICSEARCH_DETAILS, INDEX_NAME, OUTPUT_DIR, OUTPUT_FILENAME
from model import Model 

class Retriever:
    def __init__(self):
        self.es_instance = Elasticsearch(
            hosts=[ELASTICSEARCH_DETAILS['url']],
            http_auth=(ELASTICSEARCH_DETAILS['username'], ELASTICSEARCH_DETAILS['password']),
            verify_certs=False
        )
        self.index_name = INDEX_NAME
        self.url = ELASTICSEARCH_DETAILS['url'] + f"/{INDEX_NAME}/_search"
        self.username = ELASTICSEARCH_DETAILS['username']
        self.password = ELASTICSEARCH_DETAILS['password']
        self.filename = os.path.join(OUTPUT_DIR, OUTPUT_FILENAME)
    
    def retrieve_passages(self, question_embedding, question):
        data = {
            "size": 3,
            "query": {
                "script_score": {
                    "query": {"match_all": {}},
                    "script": {
                        "source": "cosineSimilarity(params.query_vector, 'Embedding') + 1.0",
                        "params": {"query_vector": question_embedding}
                    }
                }
            }
        }
        
        response = requests.post(
            self.url,
            headers={"Content-Type": "application/json"},
            auth=HTTPBasicAuth(self.username, self.password),
            verify=False,
            data=json.dumps(data)
        )
        
        if response.status_code != 200:
            print(f"Failed to retrieve documents. Error: {response.text}")
            return []
        
        return response.json()['hits']['hits']
    
    def write_to_csv(self, rows):
        with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                'Question', 'Passage 1', 'Relevance Score 1', 'Passage 1 Metadata',
                'Passage 2', 'Relevance Score 2', 'Passage 2 Metadata',
                'Passage 3', 'Relevance Score 3', 'Passage 3 Metadata'
            ])
            writer.writerows(rows)
    
    def run(self, question):
        model = Model()
        question_embedding = model.model.encode([question])[0].tolist()
        
        hits = self.retrieve_passages(question_embedding, question)
        
        rows = []
        if hits:
            row = [question]
            for hit in hits:
                passage = hit['_source'].get('Passage', '')
                metadata = hit['_source'].get('Metadata', {})
                relevance_score = hit['_score']
                row.extend([passage, relevance_score, metadata])
            rows.append(row)
        
        if rows:
            self.write_to_csv(rows)
            print(f"Data has been written to {self.filename}")
        else:
            print("No data to write.")

if __name__ == "__main__":
    retriever = Retriever()
    question = input('Enter the question: ')
    retriever.run(question)
