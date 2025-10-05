import unittest
from unittest.mock import patch, MagicMock
import requests
from offline_mode_detector import OfflineModeDetector
from news_feed import NewsFeed

class TestNewsFeed(unittest.TestCase):
    @patch('requests.get')
    def test_display_cached_news_offline(self, mock_get):
        # Mock the response to simulate a network error
        mock_get.side_effect = requests.ConnectionError

        # Mock the OfflineModeDetector to return True
        with patch.object(OfflineModeDetector, 'is_offline', return_value=True):
            # Mock the NewsFeed to return cached news
            with patch.object(NewsFeed, 'get_news', return_value=[{'title': 'Cached News', 'content': 'This is cached news.'}]):
                # Create an instance of NewsFeed
                news_feed = NewsFeed()

                # Get the news
                news = news_feed.get_news()

                # Verify that the cached news is displayed
                self.assertEqual(len(news), 1)
                self.assertEqual(news[0]['title'], 'Cached News')
                self.assertEqual(news[0]['content'], 'This is cached news.')

    @patch('requests.get')
    def test_simulate_network_disconnection(self, mock_get):
        # Mock the response to simulate a network error
        mock_get.side_effect = requests.ConnectionError

        # Mock the OfflineModeDetector to return True
        with patch.object(OfflineModeDetector, 'is_offline', return_value=True):
            # Mock the NewsFeed to return cached news
            with patch.object(NewsFeed, 'get_news', return_value=[{'title': 'Cached News', 'content': 'This is cached news.'}]):
                # Create an instance of NewsFeed
                news_feed = NewsFeed()

                # Get the news
                news = news_feed.get_news()

                # Verify that the cached news is displayed
                self.assertEqual(len(news), 1)
                self.assertEqual(news[0]['title'], 'Cached News')
                self.assertEqual(news[0]['content'], 'This is cached news.')

if __name__ == '__main__':
    unittest.main()
    