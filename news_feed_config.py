# Project name: Secure7NetGuard_1.01_Offline ;
# Author: Nelsomar Barros ;
# Github: https://github.com/SecureLogic7/Secure7NetGuard ;
# Contact: Secure7NetGuard@proton.me .

import tkinter as tk
from tkinter import ttk, messagebox
import requests

# Configuration constants
NEWS_API_KEY = ""
NEWS_API_URL = ""
USER_INTERESTS = ["Technology", "Sports", "Politics"]
WINDOW_TITLE = "News Feed"
LABEL_TEXT = "Select Category:"
WRAP_LENGTH = 80
JUSTIFY = "left"
ERROR_MESSAGE = "An error occurred: "

class NewsApp:
    def __init__(self, root):
        self.root = root
        self.root.title(WINDOW_TITLE)
        self.root.geometry("800x600")

        # Configuration
        self.news_api_key = NEWS_API_KEY
        self.news_api_url = NEWS_API_URL
        self.user_interests = USER_INTERESTS
        self.current_category = tk.StringVar(value=USER_INTERESTS[0])

        # UI Setup
        self.setup_ui()

        # Fetch initial news
        self.fetch_news()

    def setup_ui(self):
        # API Key Frame
        api_frame = ttk.LabelFrame(self.root, text="API Configuration", padding=10)
        api_frame.pack(fill=tk.X, padx=10, pady=5)

        ttk.Label(api_frame, text="NewsAPI Key:").grid(row=0, column=0, sticky=tk.W)
        self.api_key_entry = ttk.Entry(api_frame, width=50)
        self.api_key_entry.grid(row=0, column=1, padx=5)
        ttk.Button(api_frame, text="Save Key", command=self.save_api_key).grid(row=0, column=2)

        # Category Selection
        category_frame = ttk.LabelFrame(self.root, text="News Categories", padding=10)
        category_frame.pack(fill=tk.X, padx=10, pady=5)

        ttk.Label(category_frame, text=LABEL_TEXT).grid(row=0, column=0, sticky=tk.W)
        category_combo = ttk.Combobox(category_frame, textvariable=self.current_category,
                                    values=self.user_interests, state="readonly")
        category_combo.grid(row=0, column=1, padx=5)
        category_combo.bind("<<ComboboxSelected>>", lambda e: self.fetch_news())

        # News Display
        self.news_frame = ttk.LabelFrame(self.root, text="Latest News", padding=10)
        self.news_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.news_text = tk.Text(self.news_frame, wrap=tk.WORD, state=tk.DISABLED)
        self.news_text.pack(fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(self.news_text)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.news_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.news_text.yview)

        # Status Bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN)
        status_bar.pack(fill=tk.X)

    def save_api_key(self):
        self.news_api_key = self.api_key_entry.get().strip()
        if not self.news_api_key:
            messagebox.showerror("Error", "Please enter a valid API key")
            return

        self.news_api_url = f"https://newsapi.org/v2/top-headlines?country=us&category={self.current_category.get().lower()}&apiKey={self.news_api_key}"
        self.fetch_news()

    def fetch_news(self):
        if not self.news_api_key:
            self.status_var.set("Please enter your NewsAPI key first")
            return

        self.status_var.set("Fetching news...")
        self.root.update()  # Force update to show loading message

        try:
            category = self.current_category.get().lower()
            url = f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={self.news_api_key}"

            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["status"] != "ok":
                raise Exception(data.get("message", "Unknown API error"))

            self.display_news(data["articles"])
            self.status_var.set(f"Showing {category} news - {len(data['articles'])} articles found")

        except requests.exceptions.RequestException as e:
            self.status_var.set(f"Network error: {str(e)}")
            messagebox.showerror("Network Error", f"Failed to fetch news: {str(e)}")
        except Exception as e:
            self.status_var.set(f"Error: {str(e)}")
            messagebox.showerror("Error", f"{ERROR_MESSAGE}{str(e)}")

    def display_news(self, articles):
        self.news_text.config(state=tk.NORMAL)
        self.news_text.delete(1.0, tk.END)

        if not articles:
            self.news_text.insert(tk.END, "No news articles found for this category.")
            self.news_text.config(state=tk.DISABLED)
            return

        for article in articles:
            title = article.get("title", "No title")
            description = article.get("description", "No description available")
            source = article.get("source", {}).get("name", "Unknown source")
            url = article.get("url", "")

            self.news_text.insert(tk.END, f"📰 {title}\n", "title")
            self.news_text.insert(tk.END, f"Source: {source}\n", "source")
            self.news_text.insert(tk.END, f"{description}\n", "description")
            if url:
                self.news_text.insert(tk.END, f"Read more: {url}\n", "url")
            self.news_text.insert(tk.END, "\n" + "-"*80 + "\n\n")

        # Configure tags for styling
        self.news_text.tag_config("title", font=("Arial", 12, "bold"))
        self.news_text.tag_config("source", font=("Arial", 10, "italic"), foreground="blue")
        self.news_text.tag_config("description", font=("Arial", 10))
        self.news_text.tag_config("url", font=("Arial", 10), foreground="purple")

        self.news_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = NewsApp(root)
    root.mainloop()

