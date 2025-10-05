// Project name: Secure7NetGuard_1.01_Offline
// Author: Nelsomar Barros
// Github: https://github.com/SecureLogic7/Secure7NetGuard
// Contact: nelsom.one8@gmail.com

class UserAuthentication {
    constructor() {
        this.users = {};
    }

    registerUser(username, password) {
        this.users[username] = password;
        console.log(`Usuário registrado: ${username}`);
    }

    authenticateUser(username, password) {
        if (this.users[username] === password) {
            console.log(`Usuário autenticado: ${username}`);
            return true;
        } else {
            console.log(`Falha na autenticação para o usuário: ${username}`);
            return false;
        }
    }

    getUser(username) {
        return this.users[username];
    }
}

module.exports = UserAuthentication;