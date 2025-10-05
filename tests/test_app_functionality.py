# Project name: Secure7NetGuard_1.01_Offline ;
# Author: Nelsomar Barros ;
# Github: https://github.com/SecureLogic7/Secure7NetGuard ;
# Contact: nelsom.one8@gmail.com .

import pytest
from unittest.mock import patch, MagicMock
from src.app.app import App

class TestAppFunctionality:
    @pytest.fixture
    def app(self):
        return App()

    def test_encrypt_decrypt_data(self, app):
        data = "test_data"
        encrypted_data = app.encrypt_data(data)
        decrypted_data = app.decrypt_data(encrypted_data)
        assert data == decrypted_data
