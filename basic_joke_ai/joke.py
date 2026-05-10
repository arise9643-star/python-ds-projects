import groq
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()
client = groq.Groq(api_key=os.getenv("GROQ_API_KEY"))
app = FastAPI()
class JokeRequest(BaseModel):
    category: str
@app.post("/joke")
def get_joke(request: JokeRequest):
    messages = [
        {"role": "system", "content": f"You are a comedian who specializes in {request.category} jokes. Keep jokes short and punchy."},
        {"role": "user", "content": "Tell me a joke"}
    ]
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    reply = response.choices[0].message.content
    return {"joke": reply}