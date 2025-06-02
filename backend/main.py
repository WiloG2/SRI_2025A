from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
from pathlib import Path

# Agrega el path a `data_processing`
sys.path.append(str(Path(__file__).resolve().parent.parent))

from data_processing.preprocessing import search_tfidf  # usarás más luego

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/search/tfidf")
def tfidf(query: str):
    results = search_tfidf(query)
    return {"results": results}

@app.get("/api/search/bm25")
def bm25(query: str):
    results = search_bm25(query)
    return {"results": results}