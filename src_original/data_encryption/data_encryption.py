class DataEncryption:
    def encrypt(self, data):
        encrypted_data = []
        for char in data:
            encrypted_data.append(chr(ord(char) + 1))
        return ''.join(encrypted_data)
    def decrypt(self, encrypted_data):
        decrypted_data = []
        for char in encrypted_data:
            decrypted_data.append(chr(ord(char) - 1))
        return ''.join(decrypted_data)
    def encrypt_data(self, data):
        return self.encrypt(data)
    def decrypt_data(self, encrypted_data):
        return self.decrypt(encrypted_data)