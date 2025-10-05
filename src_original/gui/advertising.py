import tkinter as tk
from tkinter import messagebox
import requests
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gui.news_feed import NewsFeed

API_URL = os.getenv('ADVERTISING_API_URL')

class Advertising:
    def __init__(self, master):
        self.master = master
        self.news_feed = NewsFeed(master)

    def fetch_advertising(self, ad_label):
        try:
            user_interests = self.news_feed.user_interests
            topics = ','.join(user_interests)
            response = requests.get(API_URL, params={'topics': topics})
            response.raise_for_status()
            ad_content = response.json()
            ad_label.config(text=ad_content)
        except requests.RequestException as e:
            messagebox.showerror("Error", f"Error fetching advertising: {e}")

    def show_advertising(self):
        ad_window = tk.Toplevel(self.master)
        ad_window.title("Advertising")

        ad_label = tk.Label(ad_window, text="Fetching advertising...")
        ad_label.pack(pady=10)

        self.fetch_advertising(ad_label)

if __name__ == "__main__":
    app = tk.Tk()
    advertising = Advertising(app)
    advertising.news_feed.show_topic_selection()
    app.mainloop()
