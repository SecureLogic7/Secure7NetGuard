// Secure7NetGuard Offline - Encryption Service

class EncryptionService {
    constructor() {
        this.sodium = require('libsodium-wrappers');
    }

    async encryptData(data, key) {
        await this.sodium.ready;
        const encryptedData = this.sodium.crypto_secretbox_easy(data, new Uint8Array(24), key);
        return encryptedData;
    }

    async decryptData(encryptedData, key) {
        await this.sodium.ready;
        const decryptedData = this.sodium.crypto_secretbox_open_easy(encryptedData, new Uint8Array(24), key);
        return decryptedData;
    }
}

export default EncryptionService;