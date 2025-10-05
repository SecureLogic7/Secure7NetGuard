import tkinter as tk
from tkinter import messagebox
import requests
import os
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class OfflineUpdates:
    def __init__(self, master):
        self.master = master
        self.update_url = os.getenv('UPDATE_URL', "https://example.com/update.txt")

    def download_update(self):
        print("download_update called")  # Added this line
        try:
            logger.debug(f"Downloading update from {self.update_url}")
            if self.update_url.startswith("http://") or self.update_url.startswith("https://"):
                response = requests.get(self.update_url, timeout=5)
                response.raise_for_status()
                logger.debug(f"Update downloaded successfully: {response.text}")
                return response.text
            else:
                with open(self.update_url, "r") as f:
                    content = f.read()
                    logger.debug(f"Update read successfully from file: {content}")
                    return content
        except requests.RequestException as e:
            logger.exception(f"Error downloading update from {self.update_url}")
            if self.master.winfo_exists():
                messagebox.showerror("Error", f"Error downloading update: {e}")
            return None
        except Exception as e:
            logger.exception(f"Error downloading update from {self.update_url}")
            if self.master.winfo_exists():
                messagebox.showerror("Error", f"Error downloading update: {e}")
            return None

    def check_for_updates(self):
        update_content = self.download_update()
        if update_content:
            return [update_content]
        else:
            return []

    def apply_updates(self):
        try:
            updates = self.check_for_updates()
            if updates:
                if self.master.winfo_exists():
                    messagebox.showinfo("Updates", "Applying updates...")
                for update in updates:
                    if self.master.winfo_exists():
                        messagebox.showinfo("Update", update)
                if self.master.winfo_exists():
                    messagebox.showinfo("Updates", "Updates applied successfully.")
                logger.info("Updates applied successfully.")
            else:
                if self.master.winfo_exists():
                    messagebox.showinfo("Updates", "No updates available.")
                logger.info("No updates available.")
        except Exception as e:
            logger.error("Error applying updates")
            if self.master.winfo_exists():
                messagebox.showerror("Error", f"Error applying updates: {e}")

    def show_updates(self):
        print("show_updates called")
        logger.debug("show_updates called")
        try:
            updates_window = tk.Toplevel(self.master)
            updates_window.title("Offline Updates")
        except Exception as e:
            print(f"Error creating window: {e}")
            logger.exception("Error creating window")
            return
        updates_label = tk.Label(updates_window, text="Available Updates:")
        updates_label.pack(pady=10)

        updates = self.check_for_updates()
        for update in updates:
            update_label = tk.Label(updates_window, text=update)
            update_label.pack(pady=5)

        apply_button = tk.Button(updates_window, text="Apply Updates", command=self.apply_updates)
        apply_button.pack(pady=10)

if __name__ == "__main__":
    app = tk.Tk()
    offline_updates = OfflineUpdates(app)
    offline_updates.show_updates()
    app.mainloop()

# Project name: Secure7NetGuard_1.01_Offline ;
# Author: Nelsomar Barros ;
# Github: https://github.com/SecureLogic7/Secure7NetGuard ;
# Contact: nelsom.one8@gmail.com .

