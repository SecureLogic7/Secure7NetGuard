import tkinter as tk
from tkinter import messagebox
import subprocess

class IPDetection:
    def __init__(self):
        pass

    def detect_ip(self):
        def update_ip():
            try:
                update_button.config(text="Detectando...", state=tk.DISABLED)
                result = subprocess.run(["curl", "ifconfig.me"], capture_output=True, text=True, check=True)
                ip_address = result.stdout.strip()
                messagebox.showinfo("Atualizar IP", f"Seu IP atual é: {ip_address}")
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Erro", f"Falha ao atualizar IP: {e}")
            finally:
                update_button.config(text="Atualizar IP", state=tk.NORMAL)

        ip_window = tk.Toplevel()
        ip_window.title("Detecção de IP")

        ip_label = tk.Label(ip_window, text="IP Atual: ")
        ip_label.pack(pady=10)

        update_button = tk.Button(ip_window, text="Atualizar IP", command=update_ip)
        update_button.pack(pady=10)

    def filter_traffic(self, traffic_type):
        """
        Filter network traffic based on the specified type.

        Args:
            traffic_type (str): The type of traffic to filter (e.g., 'http', 'https', 'all').
        """
        try:
            if traffic_type == 'http':
                subprocess.run(["curl", "-v", "http://example.com"], capture_output=True, text=True, check=True)
            elif traffic_type == 'https':
                subprocess.run(["curl", "-v", "https://example.com"], capture_output=True, text=True, check=True)
            elif traffic_type == 'all':
                subprocess.run(["curl", "-v", "http://example.com"], capture_output=True, text=True, check=True)
                subprocess.run(["curl", "-v", "https://example.com"], capture_output=True, text=True, check=True)
            else:
                messagebox.showerror("Erro", "Tipo de tráfego inválido")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Erro", f"Falha ao filtrar tráfego: {e}")

    def notify_user(self, message):
        """
        Notify the user with a message.

        Args:
            message (str): The message to display to the user.
        """
        messagebox.showinfo("Notificação", message)

    def disable_network_monitoring(self):
        """
        Disable network monitoring.
        """
        messagebox.showinfo("Desativar Monitoramento de Rede", "Monitoramento de rede desativado")

    def enable_network_monitoring(self):
        """
        Enable network monitoring.
        """
        messagebox.showinfo("Ativar Monitoramento de Rede", "Monitoramento de rede ativado")

    def set_traffic_filter(self, traffic_type):
        """
        Set the traffic filter based on the specified type.

        Args:
            traffic_type (str): The type of traffic to filter (e.g., 'http', 'https', 'all').
        """
        self.filter_traffic(traffic_type)

    def show_network_monitoring_controls(self):
        """
        Show controls for enabling or disabling network monitoring.
        """
        monitoring_window = tk.Toplevel()
        monitoring_window.title("Controles de Monitoramento de Rede")

        enable_button = tk.Button(monitoring_window, text="Ativar Monitoramento", command=self.enable_network_monitoring)
        enable_button.pack(pady=10)

        disable_button = tk.Button(monitoring_window, text="Desativar Monitoramento", command=self.disable_network_monitoring)
        disable_button.pack(pady=10)

        traffic_label = tk.Label(monitoring_window, text="Filtrar Tráfego:")
        traffic_label.pack(pady=10)

        traffic_var = tk.StringVar(value="all")

        http_radio = tk.Radiobutton(monitoring_window, text="HTTP", variable=traffic_var, value="http")
        http_radio.pack(pady=5)

        https_radio = tk.Radiobutton(monitoring_window, text="HTTPS", variable=traffic_var, value="https")
        https_radio.pack(pady=5)

        all_radio = tk.Radiobutton(monitoring_window, text="Todos", variable=traffic_var, value="all")
        all_radio.pack(pady=5)

        set_filter_button = tk.Button(monitoring_window, text="Definir Filtro", command=lambda: self.set_traffic_filter(traffic_var.get()))
        set_filter_button.pack(pady=10)

    def show_ip_detection(self):
        """
        Show the IP detection window.
        """
        self.detect_ip()

    def show_network_monitoring(self):
        """
        Show the network monitoring controls.
        """
        self.show_network_monitoring_controls()

    def show_ip_and_network_monitoring(self):
        """
        Show both IP detection and network monitoring controls.
        """
        self.show_ip_detection()
        self.show_network_monitoring()

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    ip_detection = IPDetection()
    ip_detection.show_ip_and_network_monitoring()
    root.mainloop()

