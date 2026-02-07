from core.templates import render_text
from core.profiles import get_profile_by_name
from core.backup import create_backup

def post_to_platform(platform, profile, text):
    print(f"[INFO] Poste auf {platform} als {profile['display_name']}:")
    print(text)
    print("--------------------------------------------------")

def run_posting(profile_name, platforms):
    profile = get_profile_by_name(profile_name)
    if not profile:
        print("Profil nicht gefunden.")
        return

    text = render_text()

    for platform in platforms:
        post_to_platform(platform, profile, text)

    create_backup()
    print("Backup erstellt.")
