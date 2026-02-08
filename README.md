# Vetamin Social MultiPoster

Ein modernes, modulares Social‑Media‑Posting‑Tool mit GUI & CLI, API‑Key‑Verwaltung, Text‑Eingabe, Profil‑System, Plattform‑Routing und Backup‑Funktion.  
Ideal für automatisiertes oder manuelles Multi‑Posting über verschiedene Plattformen.

---

## 🚀 Features

### ✔ Moderne GUI (Hell/Dunkel)
- Basierend auf `ttkbootstrap`
- Tabs für:
  - Posting
  - API‑Keys
  - Profile
  - Einstellungen
- Textfeld mit Copy/Paste, Datei‑Import
- Theme‑Wechsel (Light/Dark)

### ✔ CLI‑Modus
- Profile auswählen
- Plattformen eingeben
- Text eintippen, reinkopieren oder aus Datei laden
- API‑Keys automatisch abfragen
- Backups erstellen

### ✔ API‑Key‑System
- Speicherung in `config/api_keys.json`
- Verwaltung über GUI
- Automatische Abfrage bei fehlenden Keys

### ✔ Plattform‑Routing
Connector‑Dateien für:
- Facebook  
- Instagram  
- Telegram  
- WhatsApp Business  
- X / Twitter  
- TikTok  
- Pinterest  
- YouTube  

### ✔ Backups
Automatische ZIP‑Backups der Config‑Dateien.

---

## 📁 Projektstruktur

```
Vetamin_Social_MultiPoster-/
│
├── start_cli.bat
├── start_gui.bat
│
├── src/
│   ├── main.py
│   ├── gui/
│   │   └── app.py
│   ├── ui/
│   │   └── cli.py
│   ├── core/
│   │   ├── posting_engine.py
│   │   ├── platform_router.py
│   │   ├── profiles.py
│   │   ├── templates.py
│   │   └── backup.py
│   └── connectors/
│       ├── facebook.py
│       ├── instagram.py
│       ├── telegram.py
│       ├── whatsapp_business.py
│       ├── x_twitter.py
│       ├── tiktok.py
│       ├── pinterest.py
│       └── youtube.py
│
├── config/
│   ├── profiles.json
│   ├── templates.json
│   ├── settings.json
│   └── api_keys.json
│
├── backups/
│   └── .keep
│
└── README.md
```

---

## ▶ Starten (Windows)

### **GUI starten**
```
start_gui.bat
```

### **CLI starten**
```
start_cli.bat
```

Beide Dateien prüfen automatisch:
- ob Python installiert ist  
- ob `ttkbootstrap` vorhanden ist (GUI)  
- und starten dann das Tool  

---

## 📝 Text eingeben

Der User kann:
- tippen  
- reinkopieren  
- mehrzeilig schreiben  
- Datei laden  
- Templates nutzen  

---

## 🔑 API‑Keys

Gespeichert in:

```
config/api_keys.json
```

Eingabe über:
- GUI (Tab „API‑Keys“)
- CLI (automatische Abfrage)

---

## 🛠 EXE erstellen (optional)

### 1. PyInstaller installieren
```
pip install pyinstaller
```

### 2. CLI‑EXE bauen
```
pyinstaller --onefile --noconsole -n VetaminCLI src/main.py
```

### 3. GUI‑EXE bauen
```
pyinstaller --onefile --windowed -n VetaminGUI src/gui/app.py
```

### 4. WICHTIG  
Folgende Ordner müssen neben der EXE liegen:

```
config/
backups/
src/connectors/
src/core/
src/ui/
```

---

## 📜 Lizenz
Privates Projekt. Nicht zur Weitergabe bestimmt.

---

## 👤 Autor
Christian (deranderechris)

