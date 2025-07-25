# app/main.py
from fastapi import FastAPI, UploadFile, File, Form
from app.modules.query_parser import parse_query
from PyPDF2 import PdfReader
import io

app = FastAPI()

@app.get("/")
def root():
    return {"message": "LLM Query System is Running"}

@app.post("/query/")
async def process_query(query: str = Form(...)):
    parsed = parse_query(query)
    return parsed

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    reader = PdfReader(io.BytesIO(contents))
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return {"extracted_text": text[:1000]} 