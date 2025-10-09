# Project name: Secure7NetGuard_1.01_Offline
# Author: Nelsomar Barros
# Github: https://github.com/SecureLogic7/Secure7NetGuard
# Contact: Secure7NetGuard@proton.me

#!/usr/bin/env python3
# main.py

import tkinter as tk
from tkinter import messagebox, ttk
import threading
import time
import logging

# Importar módulos personalizados
from tor_manager import TorManager
from network_utils import NetworkUtils

class TorPrivoxyAutomationApp:
    def __init__(self, master):
        """
        Inicializa a aplicação principal

        Args:
            master (tk.Tk): Janela principal do Tkinter
        """
        self.master = master
        self.master.title("Tor Privoxy Automation")
        self.master.geometry("600x500")

        # Configurar logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s: %(message)s'
        )
        self.logger = logging.getLogger(__name__)

        # Inicializar gerenciadores
        self.tor_manager = TorManager()
        self.network_utils = NetworkUtils()

        # Variáveis de estado
        self.is_tor_active = tk.BooleanVar(value=False)
        self.current_ip = tk.StringVar(value="Não conectado")

        # Configurar interface
        self._create_widgets()

    def _create_widgets(self):
        """
        Cria os elementos da interface gráfica
        """
        # Frame de Status
        status_frame = ttk.LabelFrame(self.master, text="Status da Conexão")
        status_frame.pack(padx=10, pady=10, fill="x")

        # Labels de Status
        ttk.Label(status_frame, text="Status Tor:").grid(row=0, column=0, sticky="w")
        status_label = ttk.Label(status_frame, textvariable=self.is_tor_active)
        status_label.grid(row=0, column=1, sticky="w")

        ttk.Label(status_frame, text="Endereço IP:").grid(row=1, column=0, sticky="w")
        ip_label = ttk.Label(status_frame, textvariable=self.current_ip)
        ip_label.grid(row=1, column=1, sticky="w")

        # Botões de Controle
        control_frame = ttk.Frame(self.master)
        control_frame.pack(padx=10, pady=10)

        start_btn = ttk.Button(control_frame, text="Iniciar Tor", command=self._start_tor)
        start_btn.grid(row=0, column=0, padx=5)

        stop_btn = ttk.Button(control_frame, text="Parar Tor", command=self._stop_tor)
        stop_btn.grid(row=0, column=1, padx=5)

        renew_btn = ttk.Button(control_frame, text="Trocar IP", command=self._renew_circuit)
        renew_btn.grid(row=0, column=2, padx=5)

        # Log de Eventos
        log_frame = ttk.LabelFrame(self.master, text="Log de Eventos")
        log_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.log_text = tk.Text(log_frame, height=10, width=70)
        self.log_text.pack(padx=5, pady=5)

    def _start_tor(self):
        """
        Inicia o serviço Tor
        """
        try:
            if self.tor_manager.start_tor_service():
                self.is_tor_active.set(True)
                self._update_ip()
                self._log("Serviço Tor iniciado com sucesso")
                self._start_monitoring()  # Iniciar monitoramento após iniciar o serviço Tor
            else:
                messagebox.showerror("Erro", "Falha ao iniciar serviço Tor")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro inesperado: {str(e)}")

    def _stop_tor(self):
        """
        Para o serviço Tor
        """
        try:
            if self.tor_manager.stop_tor_service():
                self.is_tor_active.set(False)
                self.current_ip.set("Não conectado")
                self._log("Serviço Tor parado com sucesso")
            else:
                messagebox.showerror("Erro", "Falha ao parar serviço Tor")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro inesperado: {str(e)}")

    def _renew_circuit(self):
        """
        Renova o circuito Tor
        """
        try:
            if self.tor_manager.renew_tor_circuit():
                self._update_ip()
                self._log("Circuito Tor renovado")
            else:
                messagebox.showwarning("Aviso", "Não foi possível renovar o circuito")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao renovar circuito: {str(e)}")

    def _update_ip(self):
        """
        Atualiza o endereço IP atual
        """
        try:
            new_ip = self.tor_manager.get_current_ip()
            if new_ip:
                self.current_ip.set(new_ip)
                self._log(f"IP atualizado: {new_ip}")
            else:
                self.current_ip.set("IP não disponível")
        except Exception as e:
            self.current_ip.set("Erro ao obter IP")
            self._log(f"Erro ao atualizar IP: {str(e)}")

    def _log(self, message: str):
        """
        Registra mensagens no log da interface

        Args:
            message (str): Mensagem a ser registrada
        """
        timestamp = time.strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"

        # Insere no widget de texto
        self.log_text.insert(tk.END, log_entry)

        # Rola para o final
        self.log_text.see(tk.END)

        # Registra no logger do Python
        self.logger.info(message)

    def _start_monitoring(self):
        """
        Inicia monitoramento em thread separada
        """
        def monitor():
            while self.is_tor_active.get():
                try:
                    # Exemplo de monitoramento de largura de banda
                    bandwidth = self.network_utils.monitor_bandwidth()
                    self._log(f"Banda: ↑{bandwidth.get('upload_speed', 0):.2f} ↓{bandwidth.get('download_speed', 0):.2f}")
                    time.sleep(10)  # Intervalo entre monitoramentos
                except Exception as e:
                    self._log(f"Erro no monitoramento: {str(e)}")
                    break

        # Inicia thread de monitoramento
        monitoring_thread = threading.Thread(target=monitor, daemon=True)
        monitoring_thread.start()

    def run(self):
        """
        Inicia a aplicação
        """
        self.master.mainloop()

def __main():
    """
    Função principal para inicialização da aplicação
    """
    root = tk.Tk()
    root.title("Tor Privoxy Automation")

    # Configurações de estilo
    style = ttk.Style()
    style.configure("TLabel", foreground="navy", font=("Arial", 10))
    style.configure("TButton", font=("Arial", 10))

    # Centralizar janela
    window_width = 650
    window_height = 550
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calcular posição central
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Criar instância da aplicação
    app = TorPrivoxyAutomationApp(root)

    # Configurações finais
    root.protocol("WM_DELETE_WINDOW", root.quit)

    # Iniciar aplicação
    app.run()

# Bloco de execução principal
if __name__ == "__main__":
    try:
        __main()
    except Exception as e:
        logging.error(f"Erro fatal na aplicação: {e}")
        # Opcional: criar log de erros
        with open('error_log.txt', 'a') as error_file:
            error_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {e}\n")

