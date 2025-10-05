import unittest
from unittest.mock import patch, mock_open, MagicMock
import tkinter as tk
from src.data_encryption import DataEncryption
from src.offline_updates.offline_updates import OfflineUpdates
import requests
from tkinter import messagebox
from src.offline_mode.offline_mode import OfflineModeDetector

class TestOfflineMode(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.offline_mode_detector = OfflineModeDetector()

    def tearDown(self):
        self.root.destroy()

    def test_news_feed_cache_behavior(self):
        # Set to online mode and fetch news
        self.offline_mode_detector.set_offline_mode(False)
        expected_news = {'news': 'Latest news'}  # Simulate fetching news
        self.offline_mode_detector.get_news_feed_content()

        # Set to offline mode
        self.offline_mode_detector.set_offline_mode(True)

        # Get news feed content in offline mode
        actual_news = self.offline_mode_detector.get_news_feed_content()

        # Assert that the cached news is displayed
        self.assertEqual(actual_news, expected_news)

    @patch('src.offline_mode.offline_mode.OfflineModeDetector.is_news_feed_enabled')
    def test_news_feed_network_disconnection(self, mock_is_news_feed_enabled):
        # Simulate network disconnection
        mock_is_news_feed_enabled.return_value = False

        # Set to online mode
        self.offline_mode_detector.set_offline_mode(False)

        # Simulate offline mode
        self.offline_mode_detector.offline_mode = True

        # Attempt to get news feed content
        news_content = self.offline_mode_detector.get_news_feed_content()

        # Assert that the news content is None (or cached content if available)
        self.assertEqual(news_content, None)

    def test_news_feed_cache_behavior_simple(self):
        # Set a cached news value
        self.offline_mode_detector.news_feed_content = {'news': 'Test cached news'}

        # Set to offline mode
        self.offline_mode_detector.set_offline_mode(True)

        # Get news feed content in offline mode
        actual_news = self.offline_mode_detector.get_news_feed_content()

        expected_news = {'news': 'Test cached news'}

        self.assertEqual(actual_news, expected_news)

