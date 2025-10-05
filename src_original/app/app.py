from flask import Flask, request, jsonify
from cryptography.fernet import Fernet

app = Flask(__name__)

# Generate a key for encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.route('/encrypt', methods=['POST'])
def encrypt_data():
    data = request.json.get('data')
    encrypted_data = cipher_suite.encrypt(data.encode())
    return jsonify({'encrypted_data': encrypted_data.decode()})

@app.route('/decrypt', methods=['POST'])
def decrypt_data():
    encrypted_data = request.json.get('encrypted_data')
    decrypted_data = cipher_suite.decrypt(encrypted_data.encode())
    return jsonify({'decrypted_data': decrypted_data.decode()})

if __name__ == '__main__':
    app.run(debug=True)

class App:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encrypt_data(self, data):
        encrypted_data = self.cipher_suite.encrypt(data.encode())
        return encrypted_data.decode()

    def decrypt_data(self, encrypted_data):
        decrypted_data = self.cipher_suite.decrypt(encrypted_data.encode())
        return decrypted_data.decode()

    def run(self):
        app.run(debug=True)
