import requests
import json
import time
import sys

URL = "http://127.0.0.1:8000/ingest"
file_path = sys.argv[1]

with open(file_path) as f:
    gps_stream = json.load(f)

for gps_data in gps_stream:
    try:
        r = requests.post(URL, json=gps_data, timeout=5)
        print("Sent:", gps_data)
        print("Status:", r.status_code)
        try:
            print("Response JSON:", r.json())
        except Exception:
            print("Raw Response:", r.text)   # fallback if not JSON
    except Exception as e:
        print("Error sending data:", e)
    time.sleep(1)
