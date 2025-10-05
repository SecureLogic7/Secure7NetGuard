import tkinter as tk
from tkinter import messagebox
import subprocess

def sound_alert():
    sound_window = tk.Toplevel()
    sound_window.title("Aviso Sonoro")

    settings_label = tk.Label(sound_window, text="Configurações: ")
    settings_label.pack(pady=10)

    play_button = tk.Button(sound_window, text="Reproduzir Aviso Sonoro", command=lambda: play_sound(settings_label))
    play_button.pack(pady=10)

def play_sound(settings_label):
    try:
        settings_label.config(text="Status: Reproduzindo aviso sonoro...")
        subprocess.run(["paplay", "/usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga"], check=True)
        settings_label.config(text="Status: Aviso sonoro reproduzido!")
        messagebox.showinfo("Aviso Sonoro", "Aviso sonoro reproduzido!")
    except subprocess.CalledProcessError as e:
        settings_label.config(text=f"Status: Falha ao reproduzir aviso sonoro: {e}")
        messagebox.showerror("Erro", f"Falha ao reproduzir aviso sonoro: {e}")