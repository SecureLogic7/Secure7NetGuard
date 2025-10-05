// Código para a tela de bloqueio

class LockScreen {
    constructor() {
        this.locked = false;
    }

    lock() {
        this.locked = true;
    }

    unlock() {
        this.locked = false;
    }

    isLocked() {
        return this.locked;
    }

    functionality() {
        return 'expected_result';
    }

    lockScreen() {
        document.getElementById('lockScreen').style.display = 'block';
    }

    unlockScreen() {
        document.getElementById('lockScreen').style.display = 'none';
    }
}

module.exports = LockScreen;
