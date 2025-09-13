from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from glob import glob

# ----------------- Load PDF Files ----------------- #
def load_pdf_files(folder_path):
    pdf_files = glob(f"{folder_path}/*.pdf")
    documents = []
    for pdf_file in pdf_files:
        loader = PyPDFLoader(pdf_file)        
        documents.extend(loader.load())     
    return documents



# ----------------- Filter Documents ----------------- #
from typing import List
from langchain.schema import Document

def filter_to_minimal_docs(docs: List[Document]) -> List[Document]:
    minimal_docs: List[Document] = []
    for doc in docs:
        src = doc.metadata.get("source") 
        minimal_docs.append(Document(
            page_content=doc.page_content, 
            metadata={"source": src}
        ))
    return minimal_docs



# ----------------- Split Documents into Chunks ----------------- #
def text_split(minimal_docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,   
        chunk_overlap=50, 
    )
    texts_chunk = text_splitter.split_documents(minimal_docs)
    return texts_chunk



# ----------------- Download Embedding Model ----------------- #
from langchain.embeddings import HuggingFaceBgeEmbeddings
import torch

def download_embeddings():
    model_name = "sentence-transformers/all-MiniLM-L6-v2" 
    embeddings = HuggingFaceBgeEmbeddings(
        model_name=model_name,
    )
    return embeddings

embeddings = download_embeddings()