import tkinter as tk
from tkinter import messagebox
import socket
import subprocess
import logging

# Configure logging
logging.basicConfig(filename='privoxy_install.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def is_port_available(port):
    """Checks if a given port is available."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        sock.bind(('127.0.0.1', port))
        return True
    except socket.error as e:
        logging.warning(f"Port {port} is unavailable: {e}")  # Log the conflict
        return False
    finally:
        sock.close()

def install_privoxy():
    privoxy_window = tk.Toplevel()
    privoxy_window.title("Instalação do Privoxy")

    # Port Configuration
    port_label = tk.Label(privoxy_window, text="Porta do Privoxy (8118 padrão):")
    port_label.pack(pady=5)
    port_entry = tk.Entry(privoxy_window)
    port_entry.insert(0, "8118")  # Default port
    port_entry.pack(pady=5)

    status_label = tk.Label(privoxy_window, text="Status: ")
    status_label.pack(pady=10)

    install_button = tk.Button(privoxy_window, text="Instalar Privoxy", command=lambda: start_installation(port_entry.get(), status_label))  # Pass port value and status_label
    install_button.pack(pady=10)

def start_installation(custom_port, status_label):
    try:
        # Validate port
        try:
            port = int(custom_port)
            if not (1 <= port <= 65535):
                raise ValueError("Número de porta inválido")
        except ValueError as e:
            messagebox.showerror("Erro", f"Porta inválida: {e}")
            return

        # Check if the port is available
        if not is_port_available(port):
            messagebox.showerror("Erro", f"A porta {port} está em uso. Por favor, escolha uma porta diferente.")
            return

        # Code to install Privoxy using the custom port
        status_label.config(text="Instalando Privoxy...")
        # Simulate Privoxy installation process with the custom port
        result = subprocess.run(['echo', f'Privoxy instalado com sucesso na porta {port}!'], capture_output=True, text=True)  # Example: Using subprocess
        messagebox.showinfo("Instalar Privoxy", f"Privoxy instalado com sucesso na porta {port}!")
        status_label.config(text="Status: Concluído")
        logging.info(f"Privoxy installed successfully on port {port}") # Log successful installation

    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao instalar Privoxy: {e}")
        status_label.config(text=f"Status: Erro - {e}")
        logging.exception("Error during Privoxy installation")  # Log the full exception
