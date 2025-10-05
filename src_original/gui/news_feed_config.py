# Secure7NetGuard News Feed Configuration

# Project name: Secure7NetGuard_1.01_Offline
# Author: Nelsomar Barros
# Github: https://github.com/SecureLogic7/Secure7NetGuard
# Contact: nelsom.one8@gmail.com

import os

# API URL for News Feed Module
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"

# User Interests for News Feed Module
USER_INTERESTS = [
    "technology",
    "science",
    "health",
    "entertainment",
    "sports",
    "business",
    "politics"
]

# Window Title for News Feed Module
WINDOW_TITLE = "News Feed"

# Label Text for News Feed Module
LABEL_TEXT = "Select your topics of interest to see the latest news."

# Wrap Length for News Feed Module
WRAP_LENGTH = 400

# Justify for News Feed Module
JUSTIFY = "left"

# Error Message for News Feed Module
ERROR_MESSAGE = "An error occurred while fetching news: {}"

# API Key for News Feed Module
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

# Ensure the API Key is set
if not NEWS_API_KEY:
    raise ValueError("NEWS_API_KEY environment variable is not set")

# Other API configurations can be added here
