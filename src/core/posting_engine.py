from core.backup import create_backup
from core.profiles import get_profile_by_name

def run_posting(profile_name, platforms, text):
    profile = get_profile_by_name(profile_name)

    if not profile:
        print("Fehler: Profil nicht gefunden.")
        return

    print("\n====================================")
    print("         POSTING STARTET")
    print("====================================")
    print(f"Profil: {profile_name}")
    print(f"Plattformen: {', '.join(platforms)}")
    print("------------------------------------")
    print("TEXT:")
    print(text)
    print("------------------------------------")

    # Hier wird später die echte API-Logik eingebaut
    for platform in platforms:
        print(f"[OK] Posting vorbereitet für: {platform}")

    create_backup()
    print("\nBackup wurde erstellt.")
    print("Posting-Vorgang abgeschlossen.")
    print("====================================\n")
