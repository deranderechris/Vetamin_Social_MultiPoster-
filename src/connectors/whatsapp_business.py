from core.posting_engine import ensure_api_key

def whatsapp_post(profile, text):
    api_key = ensure_api_key("whatsapp")

    print("\n=== WHATSAPP BUSINESS POST ===")
    print(f"Profil: {profile['display_name']}")
    print(f"API-Key: {api_key[:4]}****")
    print("Text:")
    print(text)
    print("================================\n")
