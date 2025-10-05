import tkinter as tk
from tkinter import messagebox
from .ip_change import IPChange
def main():
    try:
        root = tk.Tk()
        root.title("Secure7NetGuard Offline")

        root.grid_rowconfigure(0, weight=1)
        root.grid_rowconfigure(1, weight=1)
        root.grid_rowconfigure(2, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        root.grid_columnconfigure(2, weight=1)

        tk.Button(root, text="Sair", command=root.quit, width=20, height=5).grid(row=1, column=2, padx=10, pady=10)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start application: {str(e)}")

if __name__ == "__main__":
    main()

# Project name: Secure7NetGuard_1.01_Offline ;
# Author: Nelsomar Barros ;
# Github: https://github.com/SecureLogic7/Secure7NetGuard ;
# Contact: nelsom.one8@gmail.com .
