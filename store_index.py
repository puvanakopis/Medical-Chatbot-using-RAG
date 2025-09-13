from dotenv import load_dotenv
import os
from src.helper import load_pdf_files, filter_to_minimal_docs, text_split, download_embeddings
from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore

load_dotenv()

# ---------------- Get API keys ----------------
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY



# ---------------- PDF Processing ---------------- #
extracted_data = load_pdf_files("../data")
filter_data = filter_to_minimal_docs(extracted_data)
text_chunks = text_split(filter_data)
embeddings = download_embeddings()



# ---------------- Pinecone Setup ---------------- #
pinecone_api_key = PINECONE_API_KEY
pc = Pinecone(api_key=pinecone_api_key)

index_name = "medical-chatbot"

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384, 
        metric="cosine", 
        serverless=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(index_name)



# ---------------- Store Documents ---------------- #
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,  
    embedding=embeddings,   
    index_name=index_name,  
)