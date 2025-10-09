# Project name: Secure7NetGuard_1.01_Offline ;
# Author: Nelsomar Barros ;
# Github: https://github.com/SecureLogic7/Secure7NetGuard ;
# Contact: Secure7NetGuard@proton.me .

from src.app import app
import sys

if __name__ == '__main__':
    # Verifica se a aplicação está rodando em um executável PyInstaller
    if not getattr(sys, 'frozen', False):
        # Modo de desenvolvimento: Roda o servidor Flask
        app.run(debug=True)
    else:
        # Modo de distribuição (PyInstaller):
        # A lógica principal da aplicação (GUI, CLI, etc.) deve ser chamada aqui.
        # Evita a chamada app.run(debug=True) que quebra o executável.
        # Se a aplicação precisar de um servidor Flask, este deve ser iniciado de
        # forma controlada, ou a chamada app.run() deve ser totalmente evitada.
        pass
