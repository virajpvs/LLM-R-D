# streamlit run app.py

# OPENAI_API_KEY: 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
# huggingface api: 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

import streamlit as st
from dotenv import load_dotenv
import pickle
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os
from langchain.vectorstores import FAISS
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter

load_dotenv()

# Sidebar contents
with st.sidebar:
    st.title('LLM Chat App')
    st.write('---')
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](https://streamlit.io/)
    - [LangChain](https://python.langchain.com/)
    - [OpenAI](https://platform.openai.com/docs/models) LLM model

    ''')
    add_vertical_space(3)
    st.write('---')

load_dotenv()  # load environment variables


def main():
    st.header("Chat with PDF")
    # upload a PDF file
    pdf = st.file_uploader("Upload your PDF", type='pdf')

    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        # st.write(pdf_reader)  # show object
        # loading all the text into "text"
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        st.write(text)
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
            length_function=len
        )
        # chunks = text_splitter.split_text(text=text)
        chunks = text_splitter.create_documents(text=text)
        st.write(chunks)

        # embedding
        store_name = pdf.name[:-4]
        st.write(f'{store_name}')

        if os.path.exists(f"{store_name}.pkl"):
            with open(f"{store_name}.pkl", "rb") as f:
                VectorStore = pickle.load(f)
            st.write('Embeddings Loaded from the Disk')

        else:
            embeddings = OpenAIEmbeddings()
            VectorStore = FAISS.from_documents(chunks, embedding=embeddings)
            # VectorStore = Chroma.from_documents(chunks, embedding=embeddings)
            with open(f"{store_name}.pkl", "wb") as f:
                pickle.dump(VectorStore, f)
            st.write('Embeddings computation done.')

        def get_text_chunks(text):
            text_splitter = CharacterTextSplitter(
                separator="\n",
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len
            )
            chunks = text_splitter.split_text(text)
            return chunks
        tc = get_text_chunks(text)
        st.write(tc)


def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore


if __name__ == "__main__":
    main()
