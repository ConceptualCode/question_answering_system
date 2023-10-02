import streamlit as st
from retrieval import Retriever
from indexing import Indexer  # Import necessary classes from your project

# Initialize your classes
retriever = Retriever()
indexer = Indexer()

def app():
    st.title('Question Answering System')
    
    # Document Uploader
    st.subheader('Upload Document for Indexing')
    uploaded_file = st.file_uploader("Choose a document")
    if uploaded_file is not None:
        document = uploaded_file.read()  # Assume it’s a text file. Adapt as needed.
        # Index the uploaded document
        try:
            indexer.add_document(document)
            st.success('Document has been successfully indexed.')
        except Exception as e:
            st.error(f'Error occurred: {str(e)}')
        
    # Question Input
    st.subheader('Ask a Question')
    question = st.text_input("Enter your question here:")
    
    if question:
        try:
            results = retriever.run(question)
            
            if results:
                retrieved_passages = results.get('passages', [])
                generative_answer = results.get('generative_answer', '')
                
                if not retrieved_passages:
                    st.warning("No results found for your question.")
                else:
                    st.subheader('Retrieved Passages and Answers')
                    
                    for idx, result in enumerate(retrieved_passages, 1):
                        st.markdown(f"### Passage {idx}")
                        st.text(result.get('passage', ''))
                        st.markdown(f"**Relevance Score:** {result.get('score', '')}")
                        st.markdown(f"**Metadata:** {result.get('metadata', '')}")
                    
                if generative_answer:
                    st.markdown("### Generative AI Answer")
                    st.text(generative_answer)
                else:
                    st.warning("No result")
            
        except Exception as e:
            st.error(f'Error occurred: {str(e)}')


# Run Streamlit App
if __name__ == '__main__':
    app()
