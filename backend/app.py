from fastapi import FastAPI, Request
from detectors.anomaly_engine import AnomalyEngine
import uvicorn
import json
import os

app = FastAPI()
engine = AnomalyEngine()
LOG_FILE = "logs/alerts.log"
os.makedirs("logs", exist_ok=True)

@app.post("/ingest")
async def ingest_gps(request: Request):
    data = await request.json()
    response = engine.process_gps(data)

    if response.get("alert"):
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(response) + "\n")
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
