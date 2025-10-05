# Project name: Secure7NetGuard_1.01_Offline
# Author: Nelsomar Barros
# Github: https://github.com/SecureLogic7/Secure7NetGuard
# Contact: nelsom.one8@gmail.com

from flask_migrate import MigrateCommand
from flask_script import Manager

from src.app import app

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()