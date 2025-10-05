import tkinter as tk
from tkinter import messagebox
import subprocess
from PyQt5.QtWidgets import QProgressBar, QApplication

class IPChange:
    def __init__(self, master):
        self.master = master
        self.progress_bar = QProgressBar(self.master)
        self.progress_bar.setGeometry(30, 40, 200, 25)
        self.progress_bar.setValue(0)

    def change_ip(self):
        try:
            change_ip_window = tk.Toplevel(self.master)
            change_ip_window.title("Change IP")

            ip_label = tk.Label(change_ip_window, text="New IP: ")
            ip_label.pack(pady=10)

            change_button = tk.Button(change_ip_window, text="Change IP", command=lambda: self.change_ip_address(ip_label))
            change_button.pack(pady=10)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create IP change window: {str(e)}")

    def change_ip_address(self, ip_label):
        try:
            self.progress_bar.setValue(0)
            ip_label.config(text="Status: Changing IP...")
            subprocess.run(["sudo", "service", "tor", "restart"], check=True)
            for i in range(101):
                self.progress_bar.setValue(i)
                QApplication.processEvents()
            ip_label.config(text="Status: IP changed successfully!")
            messagebox.showinfo("Change IP", "IP changed successfully!")
        except subprocess.CalledProcessError as e:
            ip_label.config(text=f"Status: Failed to change IP: {e}")
            messagebox.showerror("Error", f"Failed to change IP: {e}")
        except Exception as e:
            ip_label.config(text=f"Status: Failed to change IP: {e}")
            messagebox.showerror("Error", f"Failed to change IP: {e}")

if __name__ == "__main__":
    app = QApplication([])
    window = tk.Tk()
    ip_change = IPChange(window)
    ip_change.change_ip()
    window.mainloop()
