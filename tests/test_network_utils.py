# Project name: Secure7NetGuard_1.01_Offline ;
# Author: Nelsomar Barros ;
# Github: https://github.com/SecureLogic7/Secure7NetGuard ;
# Contact: nelsom.one8@gmail.com .

import pytest
from unittest.mock import patch, MagicMock
from src.network_utils.network_utils import NetworkUtils

class TestNetworkUtils:
    @pytest.fixture
    def network_utils(self):
        return NetworkUtils()

    @patch('src.network_utils.network_utils.requests.get')
    def test_is_tor_exit_node(self, mock_get, network_utils):
        # Configura o mock para retornar uma resposta simulada
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "192.168.1.1"
        mock_get.return_value = mock_response

        # Testa um IP que deveria ser um nó de saída Tor
        assert network_utils.is_tor_exit_node("192.168.1.1") is True

        # Testa um IP que não deveria ser um nó de saída Tor
        mock_response.text = "192.168.1.2"
        assert network_utils.is_tor_exit_node("192.168.1.2") is False

    @patch('src.network_utils.network_utils.requests.get')
    def test_check_tor_anonymity(self, mock_get, network_utils):
        # Configura o mock para retornar uma resposta simulada
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"is_anonymous": True}
        mock_get.return_value = mock_response

        # Testa um IP privado
        assert network_utils.check_tor_anonymity("192.168.1.1") == 0

        # Testa um nó de saída Tor
        with patch.object(network_utils, 'is_tor_exit_node', return_value=True):
            assert network_utils.check_tor_anonymity("192.168.1.2") == 8

        # Testa um IP com anonimato médio
        with patch.object(network_utils, 'is_tor_exit_node', return_value=False):
            assert network_utils.check_tor_anonymity("192.168.1.3") == 5

    @patch('src.network_utils.network_utils.requests.get')
    def test_monitor_network_connection(self, mock_get, network_utils):
        # Configura o mock para retornar uma resposta simulada
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Testa uma conexão bem-sucedida
        assert network_utils.monitor_network_connection() is True

        # Testa uma conexão falha
        mock_get.side_effect = requests.RequestException
        assert network_utils.monitor_network_connection() is False
