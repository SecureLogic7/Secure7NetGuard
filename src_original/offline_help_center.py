class OfflineHelpCenter:
    def __init__(self):
        self.help_text = {
            "general": "Welcome to the Secure7NetGuard Offline Help Center. This application helps you manage your network security offline.",
            "features": "Features include network scanning, firewall configuration, and offline updates.",
            "troubleshooting": "If you encounter any issues, please refer to the troubleshooting section or contact support.",
            "contact": "For further assistance, please contact us at support@secure7netguard.com."
        }

    def get_help_text(self, section):
        return self.help_text.get(section, "Section not found.")

    def add_help_text(self, section, text):
        self.help_text[section] = text

# Example usage
if __name__ == "__main__":
    help_center = OfflineHelpCenter()
    print(help_center.get_help_text("general"))
    help_center.add_help_text("new_section", "This is a new section added dynamically.")
    print(help_center.get_help_text("new_section"))
