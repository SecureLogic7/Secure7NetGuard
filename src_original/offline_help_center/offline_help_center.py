# Offline Help Center Module

# Project name: Secure7NetGuard_1.01_Offline
# Author: Nelsomar Barros
# Github: https://github.com/SecureLogic7/Secure7NetGuard
# Contact: nelsom.one8@gmail.com

import os
import json

class OfflineHelpCenter:
    def __init__(self):
        self.help_center_data = self.load_help_center_data()

    def load_help_center_data(self):
        help_center_path = os.path.join(os.path.dirname(__file__), 'help_center_data.json')
        if os.path.exists(help_center_path):
            with open(help_center_path, 'r') as file:
                return json.load(file)
        else:
            return {}

    def get_help_content(self, topic):
        return self.help_center_data.get(topic, "Help content not available offline.")

    def add_help_content(self, topic, content):
        self.help_center_data[topic] = content
        self.save_help_center_data()

    def save_help_center_data(self):
        help_center_path = os.path.join(os.path.dirname(__file__), 'help_center_data.json')
        with open(help_center_path, 'w') as file:
            json.dump(self.help_center_data, file)

# Example usage
if __name__ == "__main__":
    help_center = OfflineHelpCenter()
    help_center.add_help_content("getting_started", "This is the getting started guide for offline mode.")
    print(help_center.get_help_content("getting_started"))