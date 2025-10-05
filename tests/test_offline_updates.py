import unittest
from unittest.mock import patch
import sys
import os
import requests

# Adicionar o caminho do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.offline_updates import OfflineUpdates

class TestOfflineUpdates(unittest.TestCase):
    def setUp(self):
        self.master = unittest.mock.Mock()
        self.offline_updates = OfflineUpdates(self.master)

    @patch('src.offline_updates.OfflineUpdates.download_update')
    def test_apply_updates_success(self, mock_download_update):
        mock_download_update.return_value = 'Update 1\nUpdate 2'
        self.offline_updates.apply_updates()
        self.master.winfo_exists.return_value = True
        self.master.messagebox = unittest.mock.Mock()

    @patch('src.offline_updates.OfflineUpdates.download_update')
    def test_apply_updates_no_updates(self, mock_download_update):
        mock_download_update.return_value = None
        self.offline_updates.apply_updates()
        self.master.winfo_exists.return_value = True
        self.master.messagebox = unittest.mock.Mock()

    @patch('src.offline_updates.offline_updates.messagebox.showinfo')
    def test_apply_updates_no_updates_message(self, mock_showinfo):
        self.offline_updates.apply_updates()
        mock_showinfo.assert_called_once_with("Updates", "No updates available.")

