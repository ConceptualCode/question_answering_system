# Author: Anthony Soronnadi

from retrieval import Retriever

def main():
    retriever = Retriever()
    question = input('Enter the question: ')
    retriever.run(question)

if __name__ == "__main__":
    main()
