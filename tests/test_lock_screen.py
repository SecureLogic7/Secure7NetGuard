# Project name: Secure7NetGuard_1.01_Offline
# Author: Nelsomar Barros
# Github: https://github.com/SecureLogic7/Secure7NetGuard
# Contact: Secure7NetGuard@proton.me

import unittest
from src.lock_screen.lock_screen import LockScreen

class TestLockScreen(unittest.TestCase):

    def setUp(self):
        self.lock_screen = LockScreen()

    def test_lock_screen_initialization(self):
        lock_screen = LockScreen()
        self.assertIsNotNone(lock_screen)

    def test_lock(self):
        result = self.lock_screen.lock()
        self.assertIsInstance(result, bool)

    def test_unlock(self):
        result = self.lock_screen.unlock("password")
        self.assertIsInstance(result, bool)

if __name__ == '__main__':
    unittest.main()

