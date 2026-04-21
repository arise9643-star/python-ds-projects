from langchain_community.document_loaders import TextLoader      
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS            
from langchain_community.embeddings import HuggingFaceEmbeddings 
import groq
import os
from dotenv import load_dotenv
load_dotenv()
client = groq.Groq(api_key=os.getenv("GROQ_API_KEY"))
loader = TextLoader("c:/Users/arnav/python.py/rag/document.txt")
load = loader.load()
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50
)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
document = text_splitter.split_documents(load)
storage = FAISS.from_documents(document,embeddings)
while True:
    user_input = input("What is your quiestion or say 'Bye' to end Chat: ")
    if user_input.lower() == "bye":
        print("GoodBye!!")
        break
    else:
        results = storage.similarity_search(user_input,k=2)
        context= "\n".join([result.page_content for result in results])
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role":"system","content":"you are a ai assistant which helps the coustomer with the data provided to you"},
            {"role":"user","content": f"context:{context}\n\nQuestion:{user_input}"}]
        )
        reply = response.choices[0].message.content
        print(f"AI assistant: {reply}")