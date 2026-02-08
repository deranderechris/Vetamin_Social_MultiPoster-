import json
import os
from core.backup import create_backup
from core.platform_router import get_platform_handler

API_FILE = "config/api_keys.json"


# ---------------------------------------------------------
# API-KEY HANDLING
# ---------------------------------------------------------

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

    # Wenn kein Key vorhanden → User nach Key fragen
    if platform not in keys or keys[platform].strip() == "":
        print(f"\nKein API‑Key für {platform} gefunden.")
        new_key = input(f"Bitte API‑Key für {platform} eingeben:\n→ ").strip()

        keys[platform] = new_key
        save_api_keys(keys)
        print(f"API‑Key für {platform} gespeichert.\n")

    return keys[platform]


# ---------------------------------------------------------
# POSTING ENGINE
# ---------------------------------------------------------

def run_posting(profile_name, platforms, text):
    profile = {"display_name": profile_name}

    print("\n====================================")
    print("         POSTING STARTET")
    print("====================================")

    for platform in platforms:
        handler = get_platform_handler(platform)

        if handler is None:
            print(f"Unbekannte Plattform: {platform}")
            continue

        # API-Key sicherstellen
        ensure_api_key(platform)

        # Connector aufrufen
        handler(profile, text)

    # Backup nach jedem Posting
    create_backup()
    print("\nBackup erstellt.")
    print("Posting abgeschlossen.")
    print("====================================\n")
