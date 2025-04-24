from fastapi import FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from transformers import pipeline
import os
from dotenv import load_dotenv
import uvicorn

load_dotenv()

model = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

class TextRequest(BaseModel):
    text: str
    token: str  

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(title="Text Classifier API", docs_url="/docs")

@app.post("/classify")
async def classify_text(request: TextRequest):
    if request.token != os.getenv("SECRET_TOKEN"): 
        raise HTTPException(status_code=403, detail="Invalid token")
    prediction = model(request.text)
    return {"prediction": prediction}

@app.get("/status")
async def get_status():
    return {"status": "ready", "model": "distilbert-base-uncased"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)