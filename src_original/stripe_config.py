# Secure7NetGuard Stripe API Configuration

# Project name: Secure7NetGuard_1.01_Offline
# Author: Nelsomar Barros
# Github: https://github.com/SecureLogic7/Secure7NetGuard
# Contact: nelsom.one8@gmail.com

import os

# API Key for Stripe Module
STRIPE_API_KEY = os.getenv('STRIPE_API_KEY')

# Ensure the API Key is set
if not STRIPE_API_KEY:
    raise ValueError("STRIPE_API_KEY environment variable is not set")

# Other API configurations can be added here
