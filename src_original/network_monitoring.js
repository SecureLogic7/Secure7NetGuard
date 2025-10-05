// Project name: Secure7NetGuard_1.01_Offline
// Author: Nelsomar Barros
// Github: https://github.com/SecureLogic7/Secure7NetGuard
// Contact: nelsom.one8@gmail.com

class NetworkMonitoring {
    constructor() {
        this.monitoring = false;
    }

    startMonitoring() {
        this.monitoring = true;
        console.log('Monitoramento de rede iniciado');
    }

    stopMonitoring() {
        this.monitoring = false;
        console.log('Monitoramento de rede parado');
    }

    isMonitoring() {
        return this.monitoring;
    }

    getNetworkStats() {
        return {
            upload: '100 MB',
            download: '500 MB',
            latency: '50 ms'
        };
    }
}

module.exports = NetworkMonitoring;