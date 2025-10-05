import unittest
import tkinter as tk
from tkinter import messagebox

class OfflineHelpCenter:
    def __init__(self, master):
        self.master = master

    def get_help_topics(self):
        help_topics = [
            "Getting Started",
            "Network Configuration",
            "Privacy Settings",
            "Troubleshooting",
            "Contact Support"
        ]
        return help_topics

    def get_help_content(self, topic):
        help_content = {
            "Getting Started": "Welcome to Secure7NetGuard Offline. This guide will help you get started with our application.",
            "Network Configuration": "This guide provides information on configuring your network settings.",
            "Privacy Settings": "Learn how to manage your privacy settings to ensure your data is secure.",
            "Troubleshooting": "Find solutions to common issues and problems you may encounter.",
            "Contact Support": "If you need further assistance, please contact our support team."
        }
        return help_content.get(topic, "Help content not available.")

    def show_help_center(self):
        help_window = tk.Toplevel(self.master)
        help_window.title("Offline Help Center")

        help_label = tk.Label(help_window, text="Select a help topic:")
        help_label.pack(pady=10)

        help_topics = self.get_help_topics()
        for topic in help_topics:
            topic_button = tk.Button(help_window, text=topic, command=lambda t=topic: self._show_help_content(t, help_window))
            topic_button.pack(pady=5)

    def _show_help_content(self, topic, help_window):
        help_content = self.get_help_content(topic)
        content_window = tk.Toplevel(help_window)
        content_window.title(topic)

        content_label = tk.Label(content_window, text=help_content)
        content_label.pack(pady=10)

class TestOfflineHelpCenter(unittest.TestCase):
    def setUp(self):
        self.master = tk.Tk()
        self.help_center = OfflineHelpCenter(self.master)

    def test_get_help_topics(self):
        result = self.help_center.get_help_topics()
        self.assertIsInstance(result, list)

    def test_get_help_content(self):
        result = self.help_center.get_help_content('Getting Started')
        self.assertIsInstance(result, str)

    def test_offline_help_center_initialization(self):
        self.assertIsNotNone(self.help_center)

    def test_show_help_center(self):
        self.help_center.show_help_center()
        self.assertTrue(True)

    def test_show_help_content(self):
        help_window = tk.Toplevel(self.master)
        self.help_center._show_help_content('Getting Started', help_window)
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()

