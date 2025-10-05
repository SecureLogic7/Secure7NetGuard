// Project name: Secure7NetGuard_1.01_Offline
// Author: Nelsomar Barros
// Github: https://github.com/SecureLogic7/Secure7NetGuard
// Contact: nelsom.one8@gmail.com

class SiteBlocking {
    constructor() {
        this.blockedSites = [];
    }

    blockSite(site) {
        this.blockedSites.push(site);
        console.log(`Site bloqueado: ${site}`);
    }

    unblockSite(site) {
        this.blockedSites = this.blockedSites.filter(s => s !== site);
        console.log(`Site desbloqueado: ${site}`);
    }

    isSiteBlocked(site) {
        return this.blockedSites.includes(site);
    }

    getBlockedSites() {
        return this.blockedSites;
    }
}

module.exports = SiteBlocking;