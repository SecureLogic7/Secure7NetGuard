import tkinter as tk
from tkinter import messagebox

class Settings:
    def __init__(self, master):
        self.master = master

    def save_settings(self, settings):
        try:
            with open("settings.txt", "w") as file:
                for key, value in settings.items():
                    file.write(f"{key}={value}\n")
            messagebox.showinfo("Settings", "Settings saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Error saving settings: {e}")

    def load_settings(self):
        settings = {}
        try:
            with open("settings.txt", "r") as file:
                for line in file:
                    key, value = line.strip().split("=")
                    settings[key] = value
            return settings
        except Exception as e:
            messagebox.showerror("Error", f"Error loading settings: {e}")
            return {}

    def show_settings(self):
        settings_window = tk.Toplevel(self.master)
        settings_window.title("Settings")

        settings = self.load_settings()

        for key, value in settings.items():
            setting_label = tk.Label(settings_window, text=f"{key}: {value}")
            setting_label.pack(pady=5)

        save_button = tk.Button(settings_window, text="Save Settings", command=lambda: self.save_settings(settings))
        save_button.pack(pady=10)

if __name__ == "__main__":
    app = tk.Tk()
    settings = Settings(app)
    app.mainloop()