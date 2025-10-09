# Project name: Secure7NetGuard_1.01_Offline
# Author: Nelsomar Barros
# Github: https://github.com/SecureLogic7/Secure7NetGuard
# Contact: Secure7NetGuard@proton.me

import os
import subprocess

# Directory to store deployment files
DEPLOYMENT_DIR = "./deployment"

# Files/directories to exclude from the deployment package
EXCLUDED_FILES = [
    ".git",
    "__pycache__",
    "*.pyc",
    "*.log",
    "*.db"
]

# Ensure the directory exists
os.makedirs(DEPLOYMENT_DIR, exist_ok=True)

# Function to deploy the beta version
def deploy_beta_version():
    # Create exclude options for tar command
    exclude_options = ' '.join([f'--exclude="{e}"' for e in EXCLUDED_FILES])

    # Command to create a beta deployment package
    command = f"tar -czvf {DEPLOYMENT_DIR}/beta_version.tar.gz {exclude_options} ."

    # Execute the command
try:
    subprocess.run(command, shell=True, check=True)
    print("Beta version deployed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Failed to deploy beta version: {e}")

# Example usage
if __name__ == "__main__":
    deploy_beta_version()