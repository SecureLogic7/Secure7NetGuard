import libsodium

class DataEncryption:
    def __init__(self):
        self.key = libsodium.crypto_secretbox_keygen()

    def encrypt(self, data):
        nonce = libsodium.randombytes_buf(libsodium.crypto_secretbox_NONCEBYTES)
        encrypted = libsodium.crypto_secretbox_easy(data.encode(), nonce, self.key)
        return nonce + encrypted

    def decrypt(self, encrypted_data):
        nonce = encrypted_data[:libsodium.crypto_secretbox_NONCEBYTES]
        encrypted = encrypted_data[libsodium.crypto_secretbox_NONCEBYTES:]
        decrypted = libsodium.crypto_secretbox_open_easy(encrypted, nonce, self.key)
        return decrypted.decode()
