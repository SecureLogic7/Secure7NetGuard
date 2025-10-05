const fs = require('fs');
const { exec } = require('child_process');
function blockSitesApps(sites, apps) {
    const hostsPath = '/etc/hosts';
    const hostsContent = fs.readFileSync(hostsPath, 'utf8');

    sites.forEach(site => {
        if (!hostsContent.includes(site)) {
            fs.appendFileSync(hostsPath, `\n127.0.0.1 ${site}`);
        }
    });

    apps.forEach(app => {
        exec(`sudo iptables -A OUTPUT -p tcp -d ${app} -j DROP`, (error, stdout, stderr) => {
            if (error) {
                console.error(`Error blocking ${app}: ${error}`);
                return;
            }
            console.log(`Blocked ${app}`);
        });
    });
}

function unblockSitesApps(sites, apps) {
    const hostsPath = '/etc/hosts';
    let hostsContent = fs.readFileSync(hostsPath, 'utf8');

    sites.forEach(site => {
        hostsContent = hostsContent.replace(new RegExp(`127\\.0\\.0\\.1\\s+${site}\\s*\\n?`, 'g'), '');
    });

    fs.writeFileSync(hostsPath, hostsContent);

    apps.forEach(app => {
        exec(`sudo iptables -D OUTPUT -p tcp -d ${app} -j DROP`, (error, stdout, stderr) => {
            if (error) {
                console.error(`Error unblocking ${app}: ${error}`);
                return;
            }
            console.log(`Unblocked ${app}`);
        });
    });
}
module.exports = {
    blockSitesApps,
    unblockSitesApps
};