# Project name: Secure7NetGuard_1.01_Offline ;
# Author: Nelsomar Barros ;
# Github: https://github.com/SecureLogic7/Secure7NetGuard ;
# Contact: Secure7NetGuard@proton.me .

import unittest

from src.network_monitoring.network_monitoring import NetworkMonitoring

class TestNetworkMonitoring(unittest.TestCase):

    def setUp(self):
        self.network_monitoring = NetworkMonitoring()

    def test_network_monitoring_initialization(self):
        network_monitoring = NetworkMonitoring()
        self.assertIsNotNone(network_monitoring)

    def test_monitor_network(self):
        result = self.network_monitoring.monitor_network()
        self.assertIsInstance(result, bool)

    def test_get_network_status(self):
        result = self.network_monitoring.get_network_status()
        self.assertIsInstance(result, str)
        self.assertEqual(result, "online")

    def test_get_ip_address(self):
        result = self.network_monitoring.get_ip_address()
        self.assertIsInstance(result, str)
    def test_get_network_speed(self):
        result = self.network_monitoring.get_network_speed()
        self.assertIsInstance(result, float)
    def test_get_network_status_offline(self):
        self.network_monitoring._offline = True
        result = self.network_monitoring.get_network_status()
        self.assertIsInstance(result, str)
    def test_get_ip_address_error(self):
        self.network_monitoring._offline = True
        result = self.network_monitoring.get_ip_address()
        self.assertIsInstance(result, str)
if __name__ == '__main__':
    unittest.main()

