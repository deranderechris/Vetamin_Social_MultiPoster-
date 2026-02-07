import json

def load_profiles():
    with open("config/profiles.json", "r", encoding="utf-8") as f:
        return json.load(f)
