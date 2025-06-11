from fastapi import FastAPI
from fastapi.responses import JSONResponse
@app.head("/")
def root_head():
    return JSONResponse(content={"message": "Backend API is live."})
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()
@app.get("/meldingen")
def get_meldingen():
    df = pd.read_csv("m2m_meldingen_logisch.csv")
    return df.to_dict(orient="records")
def get_meldingen():

# CORS instellen zodat frontend toegang krijgt tot deze API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # of specifieker: ["http://localhost:3000", "https://meldkamer-frontend.vercel.app"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cache de data bij opstarten (optioneel)
DATA_PATH = "m2m_meldingen_logisch.csv"

@app.get("/")
def read_root():
    return {"message": "Backend API is live."}

@app.get("/meldingen")
def get_meldingen():
    try:
        df = pd.read_csv(DATA_PATH)
        return df.to_dict(orient="records")
    except FileNotFoundError:
        return {"error": f"Bestand niet gevonden op pad: {DATA_PATH}"}
    except Exception as e:
        return {"error": str(e)}
