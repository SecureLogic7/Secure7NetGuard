# Secure7NetGuard_1.01_Offline
# Author: Nelsomar Barros
# Github: https://github.com/SecureLogic7/Secure7NetGuard
# Contact: nelsom.one8@gmail.com

import os
import subprocess
import sys
import platform
import logging
import stem
from stem.control import Controller

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TorController:
    def __init__(self, control_port=9051, socks_port=9050):
        self.control_port = control_port
        self.socks_port = socks_port
        self.logger = logging.getLogger(__name__)

    def start_tor(self):
        """Start the Tor service."""
        try:
            self.logger.info("Starting Tor service...")
            if platform.system() == 'Linux':
                subprocess.run(['sudo', 'service', 'tor', 'start'], check=True)
            elif platform.system() == 'Windows':
                subprocess.run(['net', 'start', 'tor'], check=True)
            elif platform.system() == 'Darwin':
                subprocess.run(['brew', 'services', 'start', 'tor'], check=True)
            else:
                self.logger.error(f"Unsupported operating system: {platform.system()}")
                raise Exception(f"Unsupported operating system: {platform.system()}")
            self.logger.info("Tor service started successfully.")
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to start Tor service: {e}")
            raise

    def stop_tor(self):
        """Stop the Tor service."""
        try:
            self.logger.info("Stopping Tor service...")
            if platform.system() == 'Linux':
                subprocess.run(['sudo', 'service', 'tor', 'stop'], check=True)
            elif platform.system() == 'Windows':
                subprocess.run(['net', 'stop', 'tor'], check=True)
            elif platform.system() == 'Darwin':
                subprocess.run(['brew', 'services', 'stop', 'tor'], check=True)
            else:
                self.logger.error(f"Unsupported operating system: {platform.system()}")
                raise Exception(f"Unsupported operating system: {platform.system()}")
            self.logger.info("Tor service stopped successfully.")
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to stop Tor service: {e}")
            raise

    def change_ip(self):
        """Change the IP address using Tor."""
        try:
            self.logger.info("Changing IP address using Tor...")
            with Controller.from_port(port=self.control_port) as controller:
                controller.authenticate()
                controller.signal(stem.Signal.NEWNYM)
            self.logger.info("IP address changed successfully.")
        except Exception as e:
            self.logger.error(f"Failed to change IP address: {e}")
            raise

if __name__ == "__main__":
    tor_controller = TorController()
    tor_controller.start_tor()
    tor_controller.change_ip()
    tor_controller.stop_tor()
