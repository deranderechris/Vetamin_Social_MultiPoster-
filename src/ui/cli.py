from core.profiles import list_profiles
from core.posting_engine import run_posting

def start_cli():
    print("====================================")
    print("   Vetamin Social MultiPoster")
    print("====================================")

    profiles = list_profiles()
    if not profiles:
        print("Keine Profile gefunden. Bitte lege zuerst Profile in config/profiles.json an.")
        return

    print("\nVerfügbare Profile:")
    for i, p in enumerate(profiles, start=1):
        print(f"{i}) {p}")

    auswahl = input("\nProfil auswählen (Name eingeben): ").strip()
    if auswahl not in profiles:
        print("Profil nicht gefunden.")
        return

    print("\nPlattformen eingeben (Komma getrennt):")
    print("facebook, instagram, telegram, whatsapp, x, tiktok, pinterest, youtube")
    plattformen = input("→ ").replace(" ", "").split(",")

    print("\nPoste jetzt...")
    run_posting(auswahl, plattformen)
