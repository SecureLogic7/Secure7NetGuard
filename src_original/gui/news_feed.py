import os
from dotenv import load_dotenv
import requests
import tkinter as tk
from tkinter import messagebox

# Load environment variables
load_dotenv()

class NewsFeed:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure7NetGuard Offline")
        self.root.resizable(False, False)
        self.user_interests = []
        self.topic_vars = {}
        self.api_key = os.getenv('NEWS_API_KEY')
        self.base_url = "https://newsapi.org/v2/top-headlines"

        # Create topic selection checkboxes
        self.show_topic_selection()

        # Create buttons
        self.save_button = tk.Button(root, text="Save Interests", command=self.save_user_interests)
        self.save_button.pack(pady=10)

        self.fetch_button = tk.Button(root, text="Fetch News", command=self.show_news_feed)
        self.fetch_button.pack(pady=10)

    def fetch_news(self, news_label, topic):
        try:
            params = {
                'apiKey': self.api_key,
                'category': topic,
                'language': 'en'
            }
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            articles = data.get('articles', [])

            if not articles:
                news_label.config(text="No news articles found for this topic.")
                return

            # Display the first article title (you can modify this to show more articles)
            news_text = articles[0].get('title', 'No title available')
            news_label.config(text=news_text)

        except requests.ConnectionError:
            if self.root.winfo_exists():
                messagebox.showerror("Secure7NetGuard Offline", "Failed to connect to the server. Please check your internet connection.")
        except requests.Timeout:
            if self.root.winfo_exists():
                messagebox.showerror("Secure7NetGuard Offline", "Request timed out. Please try again later.")
        except Exception as e:
            if self.root.winfo_exists():
                messagebox.showerror("Secure7NetGuard Offline", f"An error occurred: {str(e)}")

    def save_user_interests(self):
        self.user_interests = [topic for topic, var in self.topic_vars.items() if var.get()]
        if not self.user_interests:
            if self.root.winfo_exists():
                messagebox.showinfo("Secure7NetGuard Offline", "Please select at least one interest.")
        else:
            if self.root.winfo_exists():
                messagebox.showinfo("Secure7NetGuard Offline", "Interests saved successfully!")

    def show_topic_selection(self):
        # Clear previous content
        for widget in self.root.winfo_children():
                widget.destroy()

        topics = ['technology', 'sports', 'entertainment', 'business', 'health', 'science', 'general', 'politics']
        tk.Label(self.root, text="Select your interests:").pack()

        for topic in topics:
            var = tk.BooleanVar()
            self.topic_vars[topic] = var
            tk.Checkbutton(self.root, text=topic.capitalize(), variable=var).pack()

        # Re-add buttons
        self.save_button = tk.Button(self.root, text="Save Interests", command=self.save_user_interests)
        self.save_button.pack(pady=10)

        self.fetch_button = tk.Button(self.root, text="Fetch News", command=self.show_news_feed)
        self.fetch_button.pack(pady=10)

    def show_news_feed(self):
        if not self.user_interests:
            if self.root.winfo_exists():
                messagebox.showinfo("Secure7NetGuard Offline", "Please save your interests first.")
            return
        # Clear previous news content
        for widget in self.root.winfo_children():
                widget.destroy()

        # Create a frame for the news content
        news_frame = tk.Frame(self.root)
        news_frame.pack(padx=10, pady=10)

        # Create a label to display the news
        tk.Label(news_frame, text="Latest News", font=('Arial', 14, 'bold')).pack(pady=10)
        # Fetch and display news for each selected interest
        for interest in self.user_interests:
            interest_frame = tk.Frame(news_frame)
            interest_frame.pack(fill=tk.X, pady=5)

            interest_label = tk.Label(interest_frame, text=f"{interest.capitalize()} News", font=('Arial', 12, 'bold'))
            interest_label.pack(anchor='w')

            # Create a label for each interest's news
            interest_news_label = tk.Label(interest_frame, text="Loading news...", wraplength=500, justify='left')
            interest_news_label.pack(anchor='w')
            # Fetch news for this interest
            self.fetch_news(interest_news_label, interest)

        # Add navigation buttons
        refresh_button = tk.Button(news_frame, text="Refresh", command=self.show_news_feed)
        refresh_button.pack(pady=10)

        back_button = tk.Button(news_frame, text="Back to Interests", command=self.show_topic_selection)
        back_button.pack(pady=10)

# Create the main application window
root = tk.Tk()

# Initialize the NewsFeed application
app = NewsFeed(root)

# Run the application
root.mainloop()
