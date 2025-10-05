from flask import Flask
from src.data_encryption import DataEncryption

app = Flask(__name__)

class App:
    def __init__(self):
        self.data_encryption = DataEncryption()

    def encrypt_data(self, data):
        return self.data_encryption.encrypt_data(data)
    def decrypt_data(self, encrypted_data):
        return self.data_encryption.decrypt_data(encrypted_data)
@app.route('/')
def home():
    return "Secure7NetGuard Offline"

if __name__ == '__main__':
    app.run(debug=True)

# Project name: Secure7NetGuard_1.01_Offline ;
# Author: Nelsomar Barros ;
# Github: https://github.com/SecureLogic7/Secure7NetGuard ;
# Contact: nelsom.one8@gmail.com .
