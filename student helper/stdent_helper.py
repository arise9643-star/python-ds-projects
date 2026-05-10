from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import groq
import os
import tempfile
from dotenv import load_dotenv
load_dotenv()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
vector_store = None
client = groq.Groq(api_key=os.getenv("GROQ_API_KEY"))
embeddings = HuggingFaceEmbeddings(model="all-MiniLM-L6-v2")
class messages(BaseModel):
    user_input : str
@app.post("/pdf")
async def pdf_processing(file: UploadFile = File(...)):
    global vector_store
    with tempfile.NamedTemporaryFile(delete=False,suffix=".pdf") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name
        pdf = loader.load()
    loader = PyPDFLoader(tmp_path)