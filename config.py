# Author: Anthony Soronnadi

ELASTICSEARCH_DETAILS = {
    'url': 'https://localhost:9200',
    'username': 'elastic',
    'password': '',
}

CORPUS_DIR = 'path_to_corpus_dir'
INDEX_NAME = 'passage_metadata_embeddings1_index'
OUTPUT_FILENAME = 'questions_answers1.csv'
MODEL_NAME = 'paraphrase-MiniLM-L6-v2'


# app/config.py

# Elasticsearch Configuration
ELASTICSEARCH_DETAILS = {
    'url': 'https://localhost:9200',
    'username': 'elastic',
    'password': 'kaUYrTSYLObJrhDN*mJx',
}

# Directory Paths
CORPUS_DIR = 'C:\\Users\\dsn\\Desktop\\question_answering\\corpus'
OUTPUT_DIR = 'C:\\Users\\dsn\\Desktop\\question_answering\\question_answering_system\\outputs'  # Where .csv files will be saved

# File Names
PASSAGE_METADATA_FILENAME = 'passage_metadata.csv'
EMBEDDED_PASSAGE_METADATA_FILENAME = 'passage_metadata_emb.csv'
OUTPUT_FILENAME = 'questions_answers.csv'
GENERATIVE_ANSWERS_FILENAME = 'questions_answers_gen.csv'

# Index Name
INDEX_NAME = 'passage_metadata_embeddings1_index'

# Model Name
MODEL_NAME = 'paraphrase-MiniLM-L6-v2'

# API KEY
OPENAI_API_KEY = 'your_openai_api_key'

