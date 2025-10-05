import unittest
from unittest.mock import patch
from src.app import App
from src.data_encryption import DataEncryption

class TestApp(unittest.TestCase):
    def test_app_initialization(self):
        from src.app import App # Import here to avoid circular import
        app = App()
        assert app is not None

    def test_app_functionality(self):
        from src.app import App # Import here to avoid circular import
        app = App()
        encrypted_data = app.encrypt_data("test")
        decrypted_data = app.decrypt_data(encrypted_data)
        assert decrypted_data == "test"

class TestDataEncryption(unittest.TestCase):

    def setUp(self):
        from src.data_encryption import DataEncryption # Import here to avoid circular import
        self.data_encryption = DataEncryption()

    def test_encrypt_data(self):
        result = self.data_encryption.encrypt_data("test")
        self.assertIsInstance(result, str)

    def test_decrypt_data(self):
        encrypted_data = self.data_encryption.encrypt_data("test")
        result = self.data_encryption.decrypt_data(encrypted_data)
        self.assertIsInstance(result, str)

if __name__ == "__main__":
    unittest.main()
    