# Project name: Secure7NetGuard_1.01_Offline ;
# Author: Nelsomar Barros ;
# Github: https://github.com/SecureLogic7/Secure7NetGuard ;
# Contact: nelsom.one8@gmail.com .

import requests
import tkinter as tk
from tkinter import messagebox
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class StripeIntegration:
    def __init__(self, root):
        self.root = root
        self.api_key = os.getenv('STRIPE_API_KEY')
        if not self.api_key:
            raise ValueError("STRIPE_API_KEY environment variable not set")

    def create_payment(self, amount):
        try:
            logger.info(f"Creating payment with amount: {amount}")
            response = requests.post(
                "https://api.stripe.com/v1/payment_intents",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                data={
                    "amount": amount,
                    "currency": "usd"
                }
            )
            response.raise_for_status()
            logger.info(f"Payment created successfully: {response.json()}")
            return response.json()
        except Exception as e:
            logger.error(f"Error creating payment: {e}")
            return {"error": str(e)}

    def process_payment(self):
        amount_str = tk.simpledialog.askstring("Payment", "Enter amount:")
        if amount_str:
            self._process_payment(amount_str, None)

    def _process_payment(self, amount_str, entry):
        try:
            amount = int(amount_str)
            payment_intent = self.create_payment(amount)
            if payment_intent and "clientSecret" in payment_intent:
                messagebox.showinfo("Payment", "Payment processed successfully.")
            else:
                messagebox.showerror("Error", f"Error processing payment: {payment_intent.get('error', 'Unknown error')}")
        except ValueError as e:
            messagebox.showerror("Error", f"Error processing payment: {e}")

