# Secure7NetGuard_1.01_Offline
# Author: Nelsomar Barros
# Github: https://github.com/SecureLogic7/Secure7NetGuard
# Contact: nelsom.one8@gmail.com

import os
import subprocess
import sys
import platform
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PrivoxyInstaller:
    def __init__(self):
        self.system = platform.system()
        self.logger = logging.getLogger(__name__)

    def install_privoxy(self):
        """Install Privoxy on the system."""
        try:
            if self.system == 'Linux':
                self._install_on_linux()
            elif self.system == 'Windows':
                self._install_on_windows()
            elif self.system == 'Darwin':
                self._install_on_mac()
            else:
                self.logger.error(f"Unsupported operating system: {self.system}")
                raise Exception(f"Unsupported operating system: {self.system}")
        except Exception as e:
            self.logger.error(f"Failed to install Privoxy: {e}")
            raise

    def _install_on_linux(self):
        """Install Privoxy on Linux."""
        try:
            self.logger.info("Installing Privoxy on Linux...")
            subprocess.run(['sudo', 'apt-get', 'update'], check=True)
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'privoxy'], check=True)
            self.logger.info("Privoxy installed successfully on Linux.")
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to install Privoxy on Linux: {e}")
            raise

    def _install_on_windows(self):
        """Install Privoxy on Windows."""
        try:
            self.logger.info("Installing Privoxy on Windows...")
            # Download Privoxy for Windows
            privoxy_url = "https://sourceforge.net/projects/ijbswa/files/Sources/3.0.35%20%28stable%29/privoxy-3.0.35-stable-src.tar.gz/download"
            subprocess.run(['curl', '-L', privoxy_url, '-o', 'privoxy.tar.gz'], check=True)
            subprocess.run(['tar', '-xzf', 'privoxy.tar.gz'], check=True)
            os.chdir('privoxy-3.0.35-stable')
            subprocess.run(['./configure'], check=True)
            subprocess.run(['make'], check=True)
            subprocess.run(['sudo', 'make', 'install'], check=True)
            self.logger.info("Privoxy installed successfully on Windows.")
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to install Privoxy on Windows: {e}")
            raise

    def _install_on_mac(self):
        """Install Privoxy on macOS."""
        try:
            self.logger.info("Installing Privoxy on macOS...")
            subprocess.run(['brew', 'install', 'privoxy'], check=True)
            self.logger.info("Privoxy installed successfully on macOS.")
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to install Privoxy on macOS: {e}")
            raise

if __name__ == "__main__":
    installer = PrivoxyInstaller()
    installer.install_privoxy()
