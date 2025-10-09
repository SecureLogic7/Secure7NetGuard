# Project name: Secure7NetGuard_1.01_Offline ;
# Author: Nelsomar Barros ;
# Github: https://github.com/SecureLogic7/Secure7NetGuard ;
# Contact: Secure7NetGuard@proton.me .

import pytest
from unittest.mock import patch, MagicMock
from src.offline_features.offline_features import OfflineFeatures

class TestOfflineFeatures:
    @pytest.fixture
    def offline_features(self):
        return OfflineFeatures()

    @patch('src.offline_features.offline_features.NetworkUtils.monitor_network_connection')
    def test_disable_features_offline(self, mock_monitor, offline_features):
        # Configura o mock para retornar False, simulando modo offline
        mock_monitor.return_value = False

        # Testa a desativação de recursos no modo offline
        assert offline_features.disable_features_offline() is True

    @patch('src.offline_features.offline_features.NetworkUtils.monitor_network_connection')
    def test_modify_features_offline(self, mock_monitor, offline_features):
        # Configura o mock para retornar False, simulando modo offline
        mock_monitor.return_value = False

        # Testa a modificação de recursos no modo offline
        assert offline_features.modify_features_offline() is True

    @patch('src.offline_features.offline_features.NetworkUtils.monitor_network_connection')
    def test_restore_features_online(self, mock_monitor, offline_features):
        # Configura o mock para retornar True, simulando modo online
        mock_monitor.return_value = True

        # Testa a restauração de recursos no modo online
        assert offline_features.restore_features_online() is True
