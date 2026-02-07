from core.posting_engine import ensure_api_key

def instagram_post(profile, text):
    api_key = ensure_api_key("instagram")

    print("\n=== INSTAGRAM POST ===")
    print(f"Profil: {profile['display_name']}")
    print(f"API-Key: {api_key[:4]}****")
    print("Text:")
    print(text)
    print("=======================\n")
