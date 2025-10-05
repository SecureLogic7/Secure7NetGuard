import tkinter as tk
from tkinter import messagebox
import subprocess
import hashlib
import requests

class OfflineUpdates:
    def __init__(self):
        pass

    def download_update(self, update_url):
        """
        Download an update from a trusted source (HTTPS).

        Args:
            update_url (str): The URL of the update to download.
        """
        try:
            response = requests.get(update_url, verify=True)
            response.raise_for_status()
            return response.content
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Erro", f"Falha ao baixar a atualização: {e}")
            return None

    def verify_update(self, update_content, expected_checksum):
        """
        Verify the integrity of the update using a checksum.

        Args:
            update_content (bytes): The content of the update.
            expected_checksum (str): The expected checksum of the update.
        """
        actual_checksum = hashlib.sha256(update_content).hexdigest()
        return actual_checksum == expected_checksum

    def apply_update(self, update_content):
        """
        Apply the update securely.

        Args:
            update_content (bytes): The content of the update.
        """
        try:
            with open("update.zip", "wb") as f:
                f.write(update_content)
            subprocess.run(["unzip", "update.zip"], check=True)
            messagebox.showinfo("Atualização", "Atualização aplicada com sucesso")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Erro", f"Falha ao aplicar a atualização: {e}")

    def secure_update(self, update_url, expected_checksum):
        """
        Download, verify, and apply an update securely.

        Args:
            update_url (str): The URL of the update to download.
            expected_checksum (str): The expected checksum of the update.
        """
        update_content = self.download_update(update_url)
        if update_content and self.verify_update(update_content, expected_checksum):
            self.apply_update(update_content)
        else:
            messagebox.showerror("Erro", "Falha ao verificar a integridade da atualização")

    def show_update_window(self):
        """
        Show the update window.
        """
        update_window = tk.Toplevel()
        update_window.title("Atualizações Offline")

        update_label = tk.Label(update_window, text="URL da Atualização:")
        update_label.pack(pady=10)

        update_url_entry = tk.Entry(update_window, width=50)
        update_url_entry.pack(pady=10)

        checksum_label = tk.Label(update_window, text="Checksum Esperado:")
        checksum_label.pack(pady=10)

        checksum_entry = tk.Entry(update_window, width=50)
        checksum_entry.pack(pady=10)

        update_button = tk.Button(
            update_window,
            text="Baixar e Aplicar Atualização",
            command=lambda: self.secure_update(
                update_url_entry.get(),
                checksum_entry.get()
            )
        )
        update_button.pack(pady=10)

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    offline_updates = OfflineUpdates()
    offline_updates.show_update_window()
    root.mainloop()

