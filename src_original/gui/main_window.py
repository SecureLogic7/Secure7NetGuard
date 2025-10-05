import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from src.ip_detection.ip_detection import IPDetection
from src.privoxy_installer import PrivoxyInstaller  # Changed this line
from src.tor_manager.tor_manager import start_tor
from src.sound_alert.sound_alert import sound_alert
from src.advertising.advertising import Advertising
from src.stripe_integration.stripe_integration import StripeIntegration
from src.news_feed.news_feed import NewsFeed
from src.help_center.offline_help_center import OfflineHelpCenter
from src.offline_updates.offline_updates import OfflineUpdates
from src.settings.settings import Settings

# IP Detection Module
# This module will contain the functionality for detecting IP addresses
class IPDetection:
    def __init__(self):
        pass
    def detect_ip(self):
        """Detect the current IP address."""
        # Implement IP detection logic here
        return "192.168.1.1"  # Placeholder IP address

    def is_ip_changed(self, old_ip):
        """Check if the IP address has changed."""
        current_ip = self.detect_ip()
        return current_ip != old_ip

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure7NetGuard Offline")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')

        # Add security headers to prevent clickjacking
        self.root.attributes('-topmost', True)
        self.root.protocol("WM_DELETE_WINDOW", lambda: self.root.destroy())
        self.root.tk.call('wm', 'attributes', '.', '-topmost', '1')
        self.root.tk.call('wm', 'attributes', '.', '-fullscreen', '0')

        # Create a style for the buttons
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 10), padding=10, background='#4CAF50', foreground='white')
        self.style.map('TButton', background=[('active', '#45a049')])

        # Load the logo image
        self.logo_image = Image.open("src/gui/logo.png")
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)

        self.create_main_tab()

    def create_main_tab(self):
        main_tab = tk.Frame(self.root, bg='#f0f0f0')
        main_tab.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Add the logo to the main tab
        logo_label = tk.Label(main_tab, image=self.logo_photo, bg='#f0f0f0')
        logo_label.pack(pady=10)

        # Create a frame for the buttons
        button_frame = tk.Frame(main_tab, bg='#f0f0f0')
        button_frame.pack(pady=20)

        # Create buttons with consistent styling
        ttk.Button(button_frame, text="Detectar IP", command=self.detect_ip).pack(pady=5, fill=tk.X)
        ttk.Button(button_frame, text="Instalar Privoxy", command=self.install_privoxy).pack(pady=5, fill=tk.X)
        ttk.Button(button_frame, text="Iniciar Tor", command=self.start_tor).pack(pady=5, fill=tk.X)
        ttk.Button(button_frame, text="Mudar IP", command=self.change_ip).pack(pady=5, fill=tk.X)
        ttk.Button(button_frame, text="Aviso Sonoro", command=self.sound_alert).pack(pady=5, fill=tk.X)
        ttk.Button(button_frame, text="Publicidade", command=self.show_advertising).pack(pady=5, fill=tk.X)
        ttk.Button(button_frame, text="Pagamento", command=self.process_payment).pack(pady=5, fill=tk.X)
        ttk.Button(button_frame, text="Feed de Notícias", command=self.show_news_feed).pack(pady=5, fill=tk.X)
        ttk.Button(button_frame, text="Centro de Ajuda", command=self.show_help_center).pack(pady=5, fill=tk.X)
        ttk.Button(button_frame, text="Atualizações", command=self.show_updates).pack(pady=5, fill=tk.X)
        ttk.Button(button_frame, text="Configurações", command=self.show_settings).pack(pady=5, fill=tk.X)
        ttk.Button(button_frame, text="Sair", command=self.root.quit).pack(pady=5, fill=tk.X)

        # Add a label with contact information
        contact_label = tk.Label(main_tab, text="Secure7NetGuard - Contact: support@secure7netguard.com", bg='#f0f0f0', font=('Arial', 10))
        contact_label.pack(pady=10)

    def detect_ip(self):
        try:
            ip_detection = IPDetection()
            current_ip = ip_detection.detect_ip()
            messagebox.showinfo("IP Detection", f"Current IP address: {current_ip}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to detect IP: {str(e)}")

    def install_privoxy(self):
        try:
            privoxy_installer = PrivoxyInstaller()  # Changed this line
            privoxy_installer.install()  # Changed this line
            messagebox.showinfo("Feedback", "Privoxy installation completed")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to install Privoxy: {str(e)}")

    def start_tor(self):
        try:
            start_tor()
            messagebox.showinfo("Feedback", "Tor started successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start Tor: {str(e)}")

    def change_ip(self):
        try:
            # Create the Toplevel window
            change_ip_window = tk.Toplevel(self.root)
            change_ip_window.title("Change IP")

            # Add widgets or perform IP change logic
            # For example:
            label = tk.Label(change_ip_window, text="Changing IP...")
            label.pack()

            # Perform IP change operations
            # ...
            messagebox.showinfo("Feedback", "IP change initiated")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to initiate IP change: {str(e)}")

    def sound_alert(self):
        try:
            sound_alert()
            messagebox.showinfo("Feedback", "Sound alert activated")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to activate sound alert: {str(e)}")

    def show_advertising(self):
        try:
            advertising = Advertising(self.root)
            advertising.show_advertising()
            messagebox.showinfo("Feedback", "Advertising displayed")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to display advertising: {str(e)}")

    def process_payment(self):
        try:
            stripe_integration = StripeIntegration(self.root)
            stripe_integration.process_payment()
            messagebox.showinfo("Feedback", "Payment processed successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process payment: {str(e)}")

    def show_news_feed(self):
        try:
            news_feed = NewsFeed(self.root)
            news_feed.show_news_feed()
            messagebox.showinfo("Feedback", "News feed displayed")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to display news feed: {str(e)}")

    def show_help_center(self):
        try:
            help_center = OfflineHelpCenter(self.root)
            help_center.show_help_center()
            messagebox.showinfo("Feedback", "Help center opened")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open help center: {str(e)}")

    def show_updates(self):
        try:
            updates = OfflineUpdates(self.root)
            updates.show_updates()
            messagebox.showinfo("Feedback", "Updates checked")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to check updates: {str(e)}")

    def show_settings(self):
        try:
            settings = Settings(self.root)
            settings.show_settings()
            messagebox.showinfo("Feedback", "Settings opened")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open settings: {str(e)}")

    def show_message(self, message):
        messagebox.showinfo("Information", message)

# Project name: Secure7NetGuard_1.01_Offline ;
# Author: Nelsomar Barros ;
# Github: https://github.com/SecureLogic7/Secure7NetGuard ;
# Contact: nelsom.one8@gmail.com .

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

