import json
import os 
from datetime import datetime

DATA_DIR = "static/"

def load_data(filename):
    path = DATA_DIR + filename
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return []


def save_data(data, filename):
    path = DATA_DIR + filename
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

