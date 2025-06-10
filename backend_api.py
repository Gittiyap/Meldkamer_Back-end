from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()
from fastapi import FastAPI

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/meldingen")
def get_meldingen():
    df = pd.read_csv("m2m_meldingen_logisch.csv")
    return df.to_dict(orient="records")
    
    @app.get("/")
def read_root():
    return {"message": "Backend API is live!"}
