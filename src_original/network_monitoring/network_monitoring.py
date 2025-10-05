class NetworkMonitoring:
    def __init__(self):
        self.offline_mode = False

    def monitor_network(self):
        return True

    def get_network_status(self):
        return "offline" if self.offline_mode else "online"

    def get_ip_address(self):
        return "192.168.1.1"

    def get_network_speed(self):
        return 100.0

    def set_offline_mode(self, mode):
        self.offline_mode = mode

# Project name: Secure7NetGuard_1.01_Offline ;
# Author: Nelsomar Barros ;
# Github: https://github.com/SecureLogic7/Secure7NetGuard ;
# Contact: nelsom.one8@gmail.com .
