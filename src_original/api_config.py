# Secure7NetGuard API Configuration

# Project name: Secure7NetGuard_1.01_Offline
# Author: Nelsomar Barros
# Github: https://github.com/SecureLogic7/Secure7NetGuard
# Contact: nelsom.one8@gmail.com

import os

# API Key for News Feed Module
NEWS_API_KEY = os.getenv('ae2250da97124f3ebc70335a2a917e71')

# Ensure the API Key is set
if not NEWS_API_KEY:
    raise ValueError("NEWS_API_KEY environment variable is not set")

# Other API configurations can be added here
