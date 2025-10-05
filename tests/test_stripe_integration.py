# Project name: Secure7NetGuard_1.01_Offline ;
# Author: Nelsomar Barros ;
# Github: https://github.com/SecureLogic7/Secure7NetGuard ;
# Contact: nelsom.one8@gmail.com .

import unittest
from unittest.mock import patch, MagicMock
import tkinter as tk
from src.gui.stripe_integration import StripeIntegration
import os

@patch.dict(os.environ, {'STRIPE_API_KEY': 'mock_key'})
class TestStripeIntegration(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.stripe_integration = StripeIntegration(self.root)

    def tearDown(self):
        self.root.destroy()

    @patch('src.gui.stripe_integration.StripeIntegration.create_payment')
    def test_create_payment_success(self, mock_create_payment):
        mock_create_payment.return_value = {"clientSecret": "test_client_secret"}

        result = self.stripe_integration.create_payment(1000)
        self.assertEqual(result, {"clientSecret": "test_client_secret"})

    @patch('src.gui.stripe_integration.requests.post')
    def test_create_payment_error(self, mock_post):
        mock_post.side_effect = Exception("Request error")

        result = self.stripe_integration.create_payment(1000)
        self.assertEqual(result, {"error": "Request error"})

    @patch('src.gui.stripe_integration.StripeIntegration.create_payment')
    def test_process_payment_success(self, mock_create_payment):
        mock_create_payment.return_value = {"clientSecret": "test_client_secret"}
        with patch('tkinter.messagebox.showinfo') as mock_showinfo:
            self.stripe_integration._process_payment("1000", MagicMock())
            mock_showinfo.assert_called_with("Payment", "Payment processed successfully.")

    @patch('src.gui.stripe_integration.StripeIntegration.create_payment')
    def test_process_payment_error(self, mock_create_payment):
        mock_create_payment.return_value = {"error": "Payment error"}
        with patch('tkinter.messagebox.showerror') as mock_showerror:
            self.stripe_integration._process_payment("1000", MagicMock())
            mock_showerror.assert_called_with("Error", "Error processing payment: Payment error")

    @patch('src.gui.stripe_integration.StripeIntegration.create_payment')
    def test_process_payment_invalid_amount(self, mock_create_payment):
        with patch('tkinter.messagebox.showerror') as mock_showerror:
            self.stripe_integration._process_payment("invalid", MagicMock())
            mock_showerror.assert_called_with("Error", "Error processing payment: invalid literal for int() with base 10: 'invalid'")

if __name__ == '__main__':
    unittest.main()

