from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# CORS instellen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Voeg eerst de app toe...
@app.get("/")
def read_root():
    return {"message": "Backend API is live."}

# Dan mag je ook HEAD op root toevoegen:
@app.head("/")
def root_head():
    return {"message": "Backend API is live."}

@app.get("/meldingen")
def get_meldingen():
    df = pd.read_csv("m2m_meldingen_logisch.csv")
    return df.to_dict(orient="records")
