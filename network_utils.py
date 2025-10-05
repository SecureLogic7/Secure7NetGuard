# Project name: Secure7NetGuard_1.01_Offline
# Author: Nelsomar Barros
# Github: https://github.com/SecureLogic7/Secure7NetGuard
# Contact: nelsom.one8@gmail.com

# src/network_utils.py
import requests
import socket
import logging
import ipaddress

class NetworkUtils:
    def __init__(self):
        # Configuração de logging
        logging.basicConfig(level=logging.INFO, 
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)
        self.logger.info("NetworkUtils initialized")

    def is_tor_exit_node(self, ip):
        """
        Verifica se um IP é um nó de saída do Tor
        """
        try:
            # Lista de serviços para verificação de nó de saída Tor
            tor_exit_check_services = [
                f'https://check.torproject.org/exit-addresses?ip={ip}',
                f'https://metrics.torproject.org/exonerator.html?ip={ip}'
            ]

            for service in tor_exit_check_services:
                try:
                    response = requests.get(service, timeout=5)
                    if response.status_code == 200 and ip in response.text:
                        return True
                except requests.RequestException:
                    continue

            return False
        except Exception as e:
            self.logger.error(f"Erro ao verificar nó de saída Tor: {e}")
            return False

    def check_tor_anonymity(self, ip):
        """
        Avalia o nível de anonimato baseado em características do IP
        """
        try:
            # Converte IP para objeto de endereço IP
            ip_obj = ipaddress.ip_address(ip)

            # Verifica se é um IP privado ou reservado
            if ip_obj.is_private or ip_obj.is_reserved:
                return 0

            # Verifica se é um nó de saída Tor
            if self.is_tor_exit_node(ip):
                return 8  # Alto nível de anonimato

            # Verifica geolocalização e outros fatores
            try:
                hostname = socket.gethostbyaddr(ip)[0]
                if 'tor' in hostname.lower():
                    return 6
            except (socket.herror, socket.gaierror):
                pass

            # Verifica reputação do IP (simulado)
            reputation_services = [
                'https://ip-reputation-api.example.com/check',
                'https://another-reputation-service.com/verify'
            ]

            for service in reputation_services:
                try:
                    response = requests.get(service, params={'ip': ip}, timeout=3)
                    if response.status_code == 200:
                        data = response.json()
                        if data.get('is_anonymous', False):
                            return 5
                except requests.RequestException:
                    continue

            return 2  # Baixo nível de anonimato
        except Exception as e:
            self.logger.error(f"Erro ao calcular anonimato: {e}")
            return 0

    def monitor_network_connection(self, timeout=10):
        """
        Monitora a estabilidade da conexão de rede
        """
        try:
            # Testa conexão com múltiplos servidores
            test_servers = [
                'https://www.google.com',
                'https://www.cloudflare.com',
                'https://www.github.com'
            ]

            for server in test_servers:
                try:
                    response = requests.get(server, timeout=timeout)
                    if response.status_code == 200:
                        return True
                except requests.RequestException:
                    continue

            return False
        except Exception as e:
            self.logger.error(f"Erro ao monitorar conexão: {e}")
            return False
