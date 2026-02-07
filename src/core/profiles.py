import json
import os

CONFIG_PATH = "config/profiles.json"

def load_profiles():
    if not os.path.exists(CONFIG_PATH):
        return {"profiles": []}
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_profiles(data):
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def list_profiles():
    data = load_profiles()
    return [p["display_name"] for p in data.get("profiles", [])]

def get_profile_by_name(name):
    data = load_profiles()
    for p in data.get("profiles", []):
        if p["display_name"].lower() == name.lower():
            return p
    return None
