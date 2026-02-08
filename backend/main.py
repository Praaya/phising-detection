from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Phishing Detection API running"}
