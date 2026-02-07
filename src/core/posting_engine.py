import json
import os
from core.backup import create_backup

API_FILE = "config/api_keys.json"

def load_api_keys():
    if not os.path.exists(API_FILE):
        return {}
    with open(API_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_api_keys(keys):
    with open(API_FILE, "w", encoding="utf-8") as f:
        json.dump(keys, f, indent=4, ensure_ascii=False)

def ensure_api_key(platform):
    keys = load_api_keys()

    if platform not in keys or keys[platform].strip() == "":
        print(f"\n⚠️  Kein API‑Key für {platform} gefunden.")
        new_key = input(f"Bitte API‑Key für {platform} eingeben:\n→ ").strip()

        keys[platform] = new_key
        save_api_keys(keys)
        print(f"API‑Key für {platform} gespeichert.\n")

    return keys[platform]

def post_to_platform(platform, profile, text):
    api_key = ensure_api_key(platform)

    print("\n====================================")
    print(f"POSTING AUF: {platform.upper()}")
    print("------------------------------------")
    print(f"Profil: {profile['display_name']}")
    print(f"API‑Key: {api_key[:4]}**** (versteckt)")
    print("TEXT:")
    print(text)
    print("====================================\n")

    # HIER wird später die echte API‑Anfrage eingebaut
    # Beispiel:
    # requests.post("https://api.facebook.com/...", headers={"Authorization": api_key}, data={...})

def run_posting(profile_name, platforms, text):
    profile = {"display_name": profile_name}

    print("\n====================================")
    print("         POSTING STARTET")
    print("====================================")

    for platform in platforms:
        post_to_platform(platform, profile, text)

    create_backup()
    print("Backup erstellt.")
    print("Posting abgeschlossen.")
    print("====================================\n")
