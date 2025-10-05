const notifier = require('node-notifier');
function sendSecurityNotifications(message) {
    notifier.notify({
        title: 'Security Notification',
        message: message,
        sound: true,
        wait: true
    });
}

function sendPrivacyAlerts(message) {
    notifier.notify({
        title: 'Privacy Alert',
        message: message,
        sound: true,
        wait: true
    });
}

module.exports = {
    sendSecurityNotifications,
    sendPrivacyAlerts
};