from fastapi import FastAPI
from typing import List

app = FastAPI()

# Mock databáza
weddings = [
    {"id": 1, "couple": "Janka & Peter", "date": "2025-09-10"},
    {"id": 2, "couple": "Zuzka & Adam", "date": "2025-06-14"},
]

@app.get("/")
def read_root():
    return {"message": "Vitaj v svadobnej API 🎉"}

@app.get("/weddings")
def get_weddings():
    return weddings

@app.post("/weddings")
def create_wedding(couple: str, date: str):
    new_id = len(weddings) + 1
    new_wedding = {"id": new_id, "couple": couple, "date": date}
    weddings.append(new_wedding)
    return new_wedding
