import tkinter as tk
from tkinter import messagebox
import subprocess

def start_tor():
    tor_window = tk.Toplevel()
    tor_window.title("Tor")

    status_label = tk.Label(tor_window, text="Status: ")
    status_label.pack(pady=10)

    start_button = tk.Button(tor_window, text="Iniciar Tor", command=lambda: start_tor_service(status_label))
    start_button.pack(pady=10)

    stop_button = tk.Button(tor_window, text="Parar Tor", command=lambda: stop_tor_service(status_label))
    stop_button.pack(pady=10)

def start_tor_service(status_label):
    try:
        status_label.config(text="Status: Iniciando Tor...")
        subprocess.run(["sudo", "service", "tor", "start"], check=True)
        status_label.config(text="Status: Tor iniciado com sucesso!")
        messagebox.showinfo("Iniciar Tor", "Tor iniciado com sucesso!")
    except subprocess.CalledProcessError as e:
        status_label.config(text=f"Status: Falha ao iniciar Tor: {e}")
        messagebox.showerror("Erro", f"Falha ao iniciar Tor: {e}")

def stop_tor_service(status_label):
    try:
        status_label.config(text="Status: Parando Tor...")
        subprocess.run(["sudo", "service", "tor", "stop"], check=True)
        status_label.config(text="Status: Tor parado com sucesso!")
        messagebox.showinfo("Parar Tor", "Tor parado com sucesso!")
    except subprocess.CalledProcessError as e:
        status_label.config(text=f"Status: Falha ao parar Tor: {e}")
        messagebox.showerror("Erro", f"Falha ao parar Tor: {e}")