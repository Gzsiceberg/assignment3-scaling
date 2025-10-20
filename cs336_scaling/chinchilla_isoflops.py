import json

DATA_FILE = "data/isoflops_curves.json"

if __name__ == "__main__":
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
