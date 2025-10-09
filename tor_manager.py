# Project name: Secure7NetGuard_1.01_Offline ;
# Author: Nelsomar Barros ;
# Github: https://github.com/SecureLogic7/Secure7NetGuard ;
# Contact: Secure7NetGuard@proton.me .

# src/tor_manager.py
import subprocess
import requests
import time
import logging
import os
import signal
import psutil

from src.network_utils import NetworkUtils
from src.utils import validate_ip_address

class TorManager:
    def __init__(self, tor_config_path='/etc/tor/torrc', 
                 tor_binary='/usr/bin/tor', 
                 control_port=9051, 
                 socks_port=9050):
        """
        Inicialização do gerenciador Tor
        """
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO, 
                            format='%(asctime)s - %(levelname)s: %(message)s')
        
        self.tor_config_path = tor_config_path
        self.tor_binary = tor_binary
        self.control_port = control_port
        self.socks_port = socks_port
        
        self.network_utils = NetworkUtils()
        self.tor_process = None
    
    def _find_tor_process(self):
        """
        Localiza processos Tor em execução
        """
        for proc in psutil.process_iter(['name']):
            if 'tor' in proc.info['name'].lower():
                return proc
        return None
    
    def _connect_to_tor(self):
        """
        Estabelece conexão com o serviço Tor
        """
        try:
            # Verifica se Tor já está rodando
            if self.check_tor_running():
                self.logger.info("Tor já está em execução")
                self.network_utils.log_info("Tor já está em execução")
                return True
            
            # Comando para iniciar Tor
            tor_cmd = [
                self.tor_binary,
                '-f', self.tor_config_path,
                '--controlport', str(self.control_port),
                '--socksport', str(self.socks_port)
            ]
            
            # Inicia processo Tor
            self.tor_process = subprocess.Popen(
                tor_cmd, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE
            )
            
            # Aguarda inicialização
            time.sleep(10)
            
            # Verifica status
            if not self.check_tor_running():
                self.logger.error("Falha ao iniciar Tor")
                self.network_utils.log_error("Falha ao iniciar Tor")
                return False
            
            return True
        
        except Exception as e:
            self.logger.error(f"Erro ao conectar ao Tor: {e}")
            self.network_utils.log_error(f"Erro ao conectar ao Tor: {e}")
            return False
    
    def start_tor_service(self):
        """
        Inicia o serviço Tor
        """
        try:
            return self._connect_to_tor()
        except Exception as e:
            self.logger.error(f"Erro ao iniciar serviço Tor: {e}")
            return False
    
    def stop_tor_service(self):
        """
        Para o serviço Tor
        """
        try:
            tor_proc = self._find_tor_process()
            
            if tor_proc:
                # Tenta parar graciosamente
                tor_proc.terminate()
                time.sleep(3)
                
                # Força parada se necessário
                if tor_proc.is_running():
                    tor_proc.kill()
                
                self.logger.info("Serviço Tor parado com sucesso")
                return True
            
            self.logger.info("Nenhum processo Tor encontrado")
            return False
        
        except Exception as e:
            self.logger.error(f"Erro ao parar serviço Tor: {e}")
            self.network_utils.log_error(f"Erro ao parar serviço Tor: {e}")
            return False
    
# Continuação do tor_manager.py

    def check_tor_running(self):
        """
        Verifica se o serviço Tor está em execução
        """
        try:
            # Verifica processo
            tor_proc = self._find_tor_process()
            if not tor_proc:
                return False
            
            # Testa conexão
            test_url = 'https://check.torproject.org'
            try:
                response = requests.get(test_url, 
                                        proxies={'http': 'socks5://localhost:9050',
                                                 'https': 'socks5://localhost:9050'},
                                        timeout=10)
                return response.status_code == 200
            except requests.RequestException:
                return False
        
        except Exception as e:
            self.logger.error(f"Erro ao verificar status do Tor: {e}")
            self.network_utils.log_error(f"Erro ao verificar status do Tor: {e}")
            return False
    
    def get_current_ip(self):
        """
        Obtém o endereço IP atual através do Tor
        """
        try:
            # Usa serviço de verificação de IP via Tor
            response = requests.get('https://api.ipify.org', 
                                    proxies={'http': 'socks5://localhost:9050',
                                             'https': 'socks5://localhost:9050'},
                                    timeout=10)
            return response.text.strip()
        except requests.RequestException as e:
            self.logger.error(f"Erro ao obter IP: {e}")
            self.network_utils.log_error(f"Erro ao obter IP: {e}")
            return None
    
    def renew_tor_circuit(self):
        """
        Renova o circuito Tor
        """
        try:
            # Verifica se Tor está rodando
            if not self.check_tor_running():
                self.logger.warning("Tor não está em execução")
                self.network_utils.log_warning("Tor não está em execução")
                return False
            
            # Obtém IP inicial
            initial_ip = self.get_current_ip()
            
            # Tenta renovar circuito
            try:
                # Envia sinal para renovar circuito
                subprocess.run(['killall', '-HUP', 'tor'], 
                               capture_output=True, 
                               timeout=5)
            except subprocess.CalledProcessError:
                self.logger.error("Falha ao enviar sinal para renovar circuito")
                self.network_utils.log_error("Falha ao enviar sinal para renovar circuito")
                return False
            
            # Aguarda estabilização
            time.sleep(5)
            
            # Verifica novo IP
            new_ip = self.get_current_ip()
            
            # Registra mudança de IP
            if new_ip and new_ip != initial_ip:
                self.logger.info(f"Circuito Tor renovado. IP alterado de {initial_ip} para {new_ip}")
                self.network_utils.log_info(f"Circuito Tor renovado. IP alterado de {initial_ip} para {new_ip}")
                return True
            
            return False
        
        except Exception as e:
            self.logger.error(f"Erro ao renovar circuito Tor: {e}")
            self.network_utils.log_error(f"Erro ao renovar circuito Tor: {e}")
            return False

