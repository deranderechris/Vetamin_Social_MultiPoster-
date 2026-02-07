from core.profiles import list_profiles, get_profile_by_name
from core.templates import render_text
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

    profilname = input("\nProfil auswählen (Name eingeben): ").strip()
    profile = get_profile_by_name(profilname)

    if not profile:
        print("Profil nicht gefunden.")
        return

    print("\nPlattformen eingeben (Komma getrennt):")
    print("facebook, instagram, telegram, whatsapp, x, tiktok, pinterest, youtube")
    plattformen = input("→ ").replace(" ", "").split(",")

    print("\nTextmodus wählen:")
    print("1) Rotation (aus templates.json)")
    print("2) Eigenen Text eingeben")
    modus = input("→ ")

    if modus == "1":
        text = render_text()
    else:
        text = input("\nBitte eigenen Text eingeben:\n→ ")

    print("\n--- Vorschau ---")
    print(f"Profil: {profilname}")
    print(f"Plattformen: {plattformen}")
    print("Text:")
    print(text)
    print("----------------")

    confirm = input("Posten? (j/n): ").lower()
    if confirm == "j":
        run_posting(profilname, plattformen, text)
    else:
        print("Abgebrochen.")
