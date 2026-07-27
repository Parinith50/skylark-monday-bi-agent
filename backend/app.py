from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import answer

app = FastAPI(title="Skylark BI Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

@app.get("/")
def home():
    return {
        "message": "Skylark Monday BI Agent Running"
    }

@app.post("/chat")
def chat(query: Query):

    response = answer(query.question)

    return {
        "answer": response
    }