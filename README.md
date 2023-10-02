### Project Title: Question Answering System

#### Overview:
This project is a robust Question Answering System utilizing Elasticsearch, Streamlit, and advanced Natural Language Processing (NLP) techniques. It provides an interactive user interface allowing users to upload documents and ask questions related to the uploaded documents. The system then retrieves the most relevant passages from the documents and generates precise answers using Elasticsearch and GPT2 model.

### Features:
- Document Upload & Indexing
- Relevance-based Document Retrieval
- Generative AI for Question Answering
- Streamlit-based Interactive UI
- Dockerization for Easy Deployment

### Technology Stack:
- Python
- Elasticsearch
- Streamlit
- Docker
- Transformers (by Hugging Face)

### Installation & Setup:
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/ConceptualCode/question_answering_system.git question_answering_system
   cd question_answering_system
   ```

2. **Docker Setup:**
   Ensure Docker is installed on your machine. If not, download and install from [Docker Official Site](https://docs.docker.com/get-docker/).

3. **Build the Docker Image:**
   ```sh
   docker build -t question_answering_system .
   ```

4. **Run the Docker Container:**
   ```sh
   docker run -p 8501:8501 question_answering_system
   ```

   - Here, `8501` is the local port mapped to the Streamlit app running inside the Docker container. You can use any other unused port if `8501` is occupied.

### Usage:
1. **Access the Streamlit App:**
   - Open your web browser and navigate to `http://localhost:8501` (or your chosen local port).

2. **Upload Document:**
   - Use the "Upload Document for Indexing" section to upload the document you want to index.

3. **Ask a Question:**
   - After uploading the document, navigate to the "Ask a Question" section and input your question related to the uploaded document.

4. **View Responses:**
   - The system will retrieve the most relevant passages and generate answers, which will be displayed in the "Retrieved Passages and Answers" section.

### Project Structure:
# Project Structure:

  - **retrieval.py**: Handles the retrieval of relevant documents using Elasticsearch, generating relevant responses based on user input.
    
  - **indexing.py**: Manages the indexing of uploaded documents, ensuring that each document is properly stored and retrievable.
    
  - **app.py**: Contains the Streamlit app logic and UI components, rendering the interface and managing user interactions.
    
  - **Dockerfile**: Specifies the steps to create the Docker image, ensuring the project can be easily deployed and run in any environment supporting Docker.
    
  - **model.py**: Contains model used for extracting embeddings of the document representations.
    
  - **config.py**: Holds the configuration variables and settings used throughout the project, such as Elasticsearch details and other global parameters.
    
  - **generative_ai.py**: Implements the logic for generating responses based on the retrieved documents, utilizing models like GPT-2.
    
  - **requirements.txt**: Lists all the Python libraries and packages required to run the project, allowing for easy installation of dependencies.
    
  - **gen_ai.py**: Contains code for generating ai response.
    
  - **README.md**: Offers an overview of the project, instructions for setup, usage, and any additional information relevant to developers and users.
  
### How to Run the Project:

1. Clone the project repository:
   ```sh
   git clone https://github.com/ConceptualCode/question_answering_system.git question_answering_system
   cd question_answering_system

### Project Files on GitHub:
All the project files and the latest version of this project can be found on [GitHub](https://github.com/ConceptualCode/question_answering_system.git).

### Contribution & Support:
Feel free to contribute, report issues, or make feature requests in the GitHub repository. For additional support or inquiries, you can reach out to https://www.linkedin.com/in/anthony-soronnadi/

---
