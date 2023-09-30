# Author: Anthony Soronnadi

import os
import csv
import json
from sentence_transformers import SentenceTransformer
from config import MODEL_NAME, PASSAGE_METADATA_FILENAME, EMBEDDED_PASSAGE_METADATA_FILENAME, OUTPUT_DIR

class Model:
    def __init__(self):
        self.model = SentenceTransformer(MODEL_NAME)
        self.input_file = os.path.join(OUTPUT_DIR, PASSAGE_METADATA_FILENAME)
        self.output_file = os.path.join(OUTPUT_DIR, EMBEDDED_PASSAGE_METADATA_FILENAME)
    
    def load_data(self):
        """Load Passages and Metadata from CSV File"""
        data = []
        with open(self.input_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                passage, metadata = row
                data.append((passage, json.loads(metadata)))
        return data
    
    def generate_embeddings(self, data):
        """Generate Embeddings for Given Passages"""
        passages = [passage for passage, _ in data]
        embeddings = self.model.encode(passages)
        return embeddings
    
    def save_embeddings(self, data, embeddings):
        """Save Passages, Metadata, and Corresponding Embeddings to CSV File"""
        with open(self.output_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Passage', 'Metadata', 'Embedding'])
            for (passage, metadata), embedding in zip(data, embeddings):
                writer.writerow([passage, json.dumps(metadata), json.dumps(embedding.tolist())])
    
    def run(self):
        data = self.load_data()
        embeddings = self.generate_embeddings(data)
        self.save_embeddings(data, embeddings)
        print(f"Embeddings have been saved to {self.output_file}")

if __name__ == "__main__":
    model = Model()
    model.run()