# Tor Manager Module

# Project name: Secure7NetGuard_1.01_Offline
# Author: Nelsomar Barros
# Github: https://github.com/SecureLogic7/Secure7NetGuard
# Contact: nelsom.one8@gmail.com

import os
import subprocess
import time

class TorManager:
    def __init__(self, tor_path='/usr/bin/tor'):
        self.tor_path = tor_path
        self.tor_process = None

    def start_tor(self):
        if not os.path.exists(self.tor_path):
            raise FileNotFoundError(f"Tor executable not found at {self.tor_path}")

        self.tor_process = subprocess.Popen([self.tor_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(5)  # Wait for Tor to start

    def stop_tor(self):
        if self.tor_process:
            self.tor_process.terminate()
            self.tor_process.wait()
            self.tor_process = None

    def is_running(self):
        return self.tor_process is not None and self.tor_process.poll() is None

# Example usage
if __name__ == "__main__":
    tor_manager = TorManager()
    tor_manager.start_tor()
    print("Tor is running:", tor_manager.is_running())
    tor_manager.stop_tor()
    print("Tor is running:", tor_manager.is_running())