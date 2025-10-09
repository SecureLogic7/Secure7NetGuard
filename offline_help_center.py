# Project name: Secure7NetGuard_1.01_Offline
# Author: Nelsomar Barros
# Github: https://github.com/SecureLogic7/Secure7NetGuard
# Contact: Secure7NetGuard@proton.me

import os
import json

# Directory to store offline help center content
OFFLINE_HELP_CENTER_DIR = "offline_help_center"

# Ensure the directory exists
os.makedirs(OFFLINE_HELP_CENTER_DIR, exist_ok=True)

# Function to create and store help center content
def create_offline_help_center_content():
    # Example help center content
    help_center_content = {
        "faq": [
            {
                "question": "How do I reset my password?",
                "answer": "You can reset your password by clicking on the 'Forgot Password' link on the login page."
            },
            {
                "question": "How do I update my profile?",
                "answer": "You can update your profile by going to the 'Profile' section in the settings."
            }
        ],
        "tutorials": [
            {
                "title": "Getting Started",
                "content": "This tutorial will guide you through the basics of using our application."
            },
            {
                "title": "Advanced Features",
                "content": "This tutorial covers the advanced features of our application."
            }
        ]
    }

    # Save the help center content to a file
    help_center_file_path = os.path.join(OFFLINE_HELP_CENTER_DIR, "help_center.json")
    with open(help_center_file_path, "w") as help_center_file:
        json.dump(help_center_content, help_center_file)

    print("Offline help center content created and stored successfully.")

# Function to display help center content
def display_offline_help_center_content():
    help_center_file_path = os.path.join(OFFLINE_HELP_CENTER_DIR, "help_center.json")
    
    if os.path.exists(help_center_file_path):
        with open(help_center_file_path, "r") as help_center_file:
            help_center_content = json.load(help_center_file)  # noqa: F841
            
        # Display help center content logic here
        print("Offline help center content displayed successfully.")
    else:
        print("No offline help center content found.")

# Example usage
if __name__ == "__main__":
    create_offline_help_center_content()
    display_offline_help_center_content()