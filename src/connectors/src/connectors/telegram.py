from core.posting_engine import ensure_api_key

def telegram_post(profile, text):
    api_key = ensure_api_key("telegram")

    print("\n=== TELEGRAM POST ===")
    print(f"Profil: {profile['display_name']}")
    print(f"API-Key: {api_key[:4]}****")
    print("Text:")
    print(text)
    print("======================\n")
