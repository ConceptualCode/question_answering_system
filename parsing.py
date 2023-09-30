# app/parsing.py
import os
import csv
import json
import re
import spacy
from config import CORPUS_DIR, OUTPUT_DIR, PASSAGE_METADATA_FILENAME

class Parser:
    def __init__(self):
        self.corpus_dir = CORPUS_DIR
        self.output_file = os.path.join(OUTPUT_DIR, PASSAGE_METADATA_FILENAME)
        self.nlp = spacy.load("en_core_web_sm")  # Assuming you are using English language model

    def extract_paragraphs(self, content):
        # Extracting paragraphs within __paragraph__ markers under parent __section__ markers
        paragraphs = re.findall(r'__paragraph__\n(.*?)\n(?=__paragraph__|$)', content, re.DOTALL)
        return paragraphs

    def split_into_chunks(self, paragraphs):
        # Splitting paragraphs into chunks of 5 sentences to form a passage each
        chunks = []
        for paragraph in paragraphs:
            doc = self.nlp(paragraph)
            sentences = [sent.text for sent in doc.sents]
            for i in range(0, len(sentences), 5):
                chunk = ' '.join(sentences[i:i+5])
                chunks.append(chunk)
        return chunks
    
    def parse_and_write(self):
        with open(self.output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['Passage', 'Metadata'])
            writer.writeheader()

            for filename in os.listdir(self.corpus_dir):
                if filename.endswith("_Technical.txt"):
                    base_filename = filename.replace("_Technical.txt", "")
                    metadata_filename = base_filename + "_Metadata.json"

                    with open(os.path.join(self.corpus_dir, filename), 'r', encoding='utf-8') as tech_file:
                        content = tech_file.read()
                        paragraphs = self.extract_paragraphs(content)
                        chunks = self.split_into_chunks(paragraphs)

                        with open(os.path.join(self.corpus_dir, metadata_filename), 'r', encoding='utf-8') as meta_file:
                            metadata = json.load(meta_file)
                            for chunk in chunks:
                                writer.writerow({'Passage': chunk, 'Metadata': json.dumps(metadata)})

if __name__ == '__main__':
    parser = Parser()
    parser.parse_and_write()
