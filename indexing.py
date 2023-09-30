# app/indexing.py
import os
import json
import csv
from elasticsearch import Elasticsearch, helpers
from config import ELASTICSEARCH_DETAILS, INDEX_NAME, EMBEDDED_PASSAGE_METADATA_FILENAME, OUTPUT_DIR

class Indexer:
    def __init__(self):
        self.es_instance = Elasticsearch(
            hosts=[ELASTICSEARCH_DETAILS['url']],
            http_auth=(
                ELASTICSEARCH_DETAILS['username'], ELASTICSEARCH_DETAILS['password']
            ),
            verify_certs=False,
        )
        self.index_name = INDEX_NAME
        self.csv_file_path = os.path.join(OUTPUT_DIR, EMBEDDED_PASSAGE_METADATA_FILENAME)
    
    def create_index(self):
        """Create an Elasticsearch index."""
        index_structure = {
            "mappings": {
                "properties": {
                    "Passage": {"type": "text"},
                    "Metadata": {"type": "nested"},
                    "Embedding": {"type": "dense_vector", "dims": 384}
                }
            }
        }
        
        self.es_instance.indices.create(index=self.index_name, body=index_structure)
    
    def index_data_to_elasticsearch(self):
        """Bulk index data to Elasticsearch."""
        def generate_bulk_data():
            with open(self.csv_file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    yield {
                        "_op_type": 'index',
                        "_index": self.index_name,
                        "_source": {
                            "Passage": row['Passage'],
                            "Metadata": json.loads(row['Metadata']) if row['Metadata'] != 'null' else None,
                            "Embedding": json.loads(row['Embedding'])
                        }
                    }
        helpers.bulk(self.es_instance, generate_bulk_data())
    
    def run(self):
        self.create_index()
        self.index_data_to_elasticsearch()
        print(f"Data has been indexed to {self.index_name}")

if __name__ == "__main__":
    indexer = Indexer()
    indexer.run()
