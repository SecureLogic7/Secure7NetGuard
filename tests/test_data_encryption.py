import unittest

from src.data_encryption import DataEncryption
import secrets

class TestDataEncryption(unittest.TestCase):

    def setUp(self):
        self.data_encryption = DataEncryption()

    def test_encrypt_decrypt(self):
        original_data = "my secret data"
        encrypted_data = self.data_encryption.encrypt(original_data)
        decrypted_data = self.data_encryption.decrypt(encrypted_data)
        self.assertEqual(decrypted_data, original_data)

    def test_encrypt_decrypt_data(self):
        original_data = secrets.token_hex(16)  # generate random string
        encrypted_data = self.data_encryption.encrypt(original_data)
        decrypted_data = self.data_encryption.decrypt(encrypted_data)
        self.assertEqual(decrypted_data, original_data)


if __name__ == '__main__':
    unittest.main()
