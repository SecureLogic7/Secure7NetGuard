// Código para teste da tela de bloqueio

const LockScreen = require('../../src/lock_screen.js');

describe('LockScreen', () => {
    it('should initialize correctly', () => {
        const lockScreen = new LockScreen();
        expect(lockScreen).toBeDefined();
    });

    it('should have expected functionality', () => {
        const lockScreen = new LockScreen();
        expect(lockScreen.functionality()).toBe('expected_result');
    });

    it('should lock the screen', () => {
        document.body.innerHTML = '<div id="lockScreen"></div>';
        const lockScreen = new LockScreen();
        lockScreen.lockScreen();
        expect(document.getElementById('lockScreen').style.display).toBe('block');
    });

    it('should unlock the screen', () => {
        document.body.innerHTML = '<div id="lockScreen"></div>';
        const lockScreen = new LockScreen();
        lockScreen.unlockScreen();
        expect(document.getElementById('lockScreen').style.display).toBe('none');
    });
});
