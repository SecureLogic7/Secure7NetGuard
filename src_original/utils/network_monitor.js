// Secure7NetGuard Offline - Network Monitor

class NetworkMonitor {
    constructor() {
        this.pcap = require('pcap-plus-plus');
    }

    monitorNetwork() {
        const device = this.pcap.findalldevs()[0];
        const handle = this.pcap.create(device.name);
        handle.on('packet', (rawPacket) => {
            const packet = this.pcap.decode.packet(rawPacket);
            console.log('Pacote de rede:', packet);
        });
        handle.start();
    }
}

export default NetworkMonitor;