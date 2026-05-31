import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "results.json"

def get_latest_result():
    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    return data[-1]