import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
from tkinter import filedialog, messagebox

from core.profiles import list_profiles, get_profile_by_name
from core.templates import render_text
from core.posting_engine import run_posting, load_api_keys, save_api_keys


class MultiPosterGUI:
    def __init__(self):
        self.app = ttk.Window(
            title="Vetamin Social MultiPoster",
            themename="darkly"  # darkly, flatly, litera, lumen, etc.
        )

        self.app.geometry("900x600")

        self.notebook = ttk.Notebook(self.app)
        self.notebook.pack(fill="both", expand=True)

        self.build_post_tab()
        self.build_api_tab()
        self.build_profile_tab()
        self.build_settings_tab()

    # ---------------------------------------------------------
    # POSTING TAB
    # ---------------------------------------------------------
    def build_post_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Posting")

        # Profil-Auswahl
        ttk.Label(frame, text="Profil auswählen:", font="-size 12").pack(pady=5)
        self.profile_var = tk.StringVar()
        self.profile_box = ttk.Combobox(frame, textvariable=self.profile_var)
        self.profile_box["values"] = list_profiles()
        self.profile_box.pack(pady=5)

        # Plattformen
        ttk.Label(frame, text="Plattformen (Komma getrennt):").pack(pady=5)
        self.platform_entry = ttk.Entry(frame)
        self.platform_entry.insert(0, "facebook, instagram, telegram")
        self.platform_entry.pack(fill="x", padx=20)

        # Textfeld
        ttk.Label(frame, text="Text eingeben:").pack(pady=5)
        self.text_box = tk.Text(frame, height=12)
        self.text_box.pack(fill="both", padx=20, pady=5, expand=True)

        # Buttons
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Text aus Datei laden", command=self.load_text_file).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Template verwenden", command=self.use_template).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Posten", bootstyle=SUCCESS, command=self.post).pack(side="left", padx=5)

    def load_text_file(self):
        path = filedialog.askopenfilename()
        if not path:
            return
        with open(path, "r", encoding="utf-8") as f:
            self.text_box.delete("1.0", tk.END)
            self.text_box.insert(tk.END, f.read())

    def use_template(self):
        text = render_text()
        self.text_box.delete("1.0", tk.END)
        self.text_box.insert(tk.END, text)

    def post(self):
        profile = self.profile_var.get()
        if not profile:
            messagebox.showerror("Fehler", "Bitte ein Profil auswählen.")
            return

        platforms = [p.strip() for p in self.platform_entry.get().split(",")]
        text = self.text_box.get("1.0", tk.END).strip()

        if not text:
            messagebox.showerror("Fehler", "Bitte Text eingeben.")
            return

        run_posting(profile, platforms, text)
        messagebox.showinfo("Erfolg", "Posting abgeschlossen.")

    # ---------------------------------------------------------
    # API-KEY TAB
    # ---------------------------------------------------------
    def build_api_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="API-Keys")

        ttk.Label(frame, text="API‑Keys verwalten", font="-size 14").pack(pady=10)

        self.api_entries = {}
        keys = load_api_keys()

        for platform in ["facebook", "instagram", "telegram", "whatsapp", "x", "tiktok", "pinterest", "youtube"]:
            row = ttk.Frame(frame)
            row.pack(fill="x", padx=20, pady=5)

            ttk.Label(row, text=platform.capitalize(), width=15).pack(side="left")

            var = tk.StringVar(value=keys.get(platform, ""))
            entry = ttk.Entry(row, textvariable=var, show="*")
            entry.pack(side="left", fill="x", expand=True)

            self.api_entries[platform] = var

        ttk.Button(frame, text="Speichern", bootstyle=SUCCESS, command=self.save_api_keys).pack(pady=10)

    def save_api_keys(self):
        data = {p: v.get() for p, v in self.api_entries.items()}
        save_api_keys(data)
        messagebox.showinfo("Gespeichert", "API‑Keys wurden gespeichert.")

    # ---------------------------------------------------------
    # PROFILE TAB
    # ---------------------------------------------------------
    def build_profile_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Profile")

        ttk.Label(frame, text="Profile (nur Anzeige)", font="-size 14").pack(pady=10)

        profiles = list_profiles()
        for p in profiles:
            ttk.Label(frame, text=f"• {p}", font="-size 12").pack(anchor="w", padx=20)

    # ---------------------------------------------------------
    # SETTINGS TAB
    # ---------------------------------------------------------
    def build_settings_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Einstellungen")

        ttk.Label(frame, text="Theme auswählen:", font="-size 12").pack(pady=10)

        theme_box = ttk.Combobox(frame, values=ttk.Style().theme_names())
        theme_box.set("darkly")
        theme_box.pack(pady=5)

        ttk.Button(frame, text="Theme anwenden", command=lambda: self.app.style.theme_use(theme_box.get())).pack(pady=10)

    # ---------------------------------------------------------
    # START
    # ---------------------------------------------------------
    def run(self):
        self.app.mainloop()


if __name__ == "__main__":
    gui = MultiPosterGUI()
    gui.run()
