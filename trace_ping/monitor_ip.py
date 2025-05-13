import webview
from flask import Flask, render_template, jsonify
import threading
import sqlite3
from datetime import datetime
import ping3
import json

app = Flask(__name__)

class MonitorIP:
    def __init__(self):
        self.ips_monitorados = {}
        self.threads_ativas = {}
        self.inicializar_db()
        self.carregar_ips()

    def inicializar_db(self):
        with sqlite3.connect('monitor_ip.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS eventos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ip TEXT,
                    status TEXT,
                    timestamp DATETIME,
                    duracao INTEGER
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS ips (
                    ip TEXT PRIMARY KEY,
                    descricao TEXT
                )
            ''')
            conn.commit()

    def adicionar_ip(self, ip, desc):
        with sqlite3.connect('monitor_ip.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT OR REPLACE INTO ips (ip, descricao) VALUES (?, ?)", (ip, desc))
            conn.commit()
        self.iniciar_monitoramento(ip, desc)
        return True

    def iniciar_monitoramento(self, ip, desc):
        if ip not in self.threads_ativas:
            self.ips_monitorados[ip] = {"desc": desc, "status": "Iniciando...", "ultima_verificacao": "-"}
            thread = threading.Thread(target=self.monitorar_ip, args=(ip,), daemon=True)
            self.threads_ativas[ip] = thread
            thread.start()

    def monitorar_ip(self, ip):
        ultimo_status = None
        inicio_queda = None
        
        # Adicionar atributo para controlar a execução da thread
        thread_atual = threading.current_thread()
        thread_atual.do_run = True
        
        while thread_atual.do_run:
            try:
                resposta = ping3.ping(ip, timeout=1)
                status_atual = "Online" if resposta is not None else "Offline"
                
                if status_atual != ultimo_status:
                    timestamp = datetime.now()
                    
                    if status_atual == "Offline":
                        inicio_queda = timestamp
                    elif ultimo_status == "Offline" and inicio_queda:
                        duracao = int((timestamp - inicio_queda).total_seconds())
                        self.registrar_evento(ip, "Recuperado", timestamp, duracao)
                        inicio_queda = None
                    
                    self.registrar_evento(ip, status_atual, timestamp, 0)
                    ultimo_status = status_atual
                
                self.ips_monitorados[ip]["status"] = status_atual
                self.ips_monitorados[ip]["ultima_verificacao"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                
            except Exception as e:
                print(f"Erro ao monitorar {ip}: {str(e)}")
            
            threading.Event().wait(1)

    def registrar_evento(self, ip, status, timestamp, duracao):
        with sqlite3.connect('monitor_ip.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO eventos (ip, status, timestamp, duracao) VALUES (?, ?, ?, ?)",
                (ip, status, timestamp, duracao)
            )
            conn.commit()

    def get_dispositivos(self):
        return self.ips_monitorados

    def get_historico(self, ip):
        with sqlite3.connect('monitor_ip.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT timestamp, status, duracao FROM eventos WHERE ip = ? ORDER BY timestamp DESC LIMIT 100",
                (ip,)
            )
            eventos = []
            for timestamp, status, duracao in cursor.fetchall():
                eventos.append({
                    "timestamp": datetime.fromisoformat(timestamp).strftime("%d/%m/%Y %H:%M:%S"),
                    "status": status,
                    "duracao": duracao
                })
            return eventos

    def remover_ip(self, ip):
        with sqlite3.connect('monitor_ip.db') as conn:
            cursor = conn.cursor()
            # Remover o IP da tabela de IPs
            cursor.execute("DELETE FROM ips WHERE ip = ?", (ip,))
            # Remover todos os eventos relacionados ao IP
            cursor.execute("DELETE FROM eventos WHERE ip = ?", (ip,))
            conn.commit()
        
        # Parar o monitoramento removendo das estruturas de dados
        if ip in self.ips_monitorados:
            del self.ips_monitorados[ip]
        if ip in self.threads_ativas:
            # Marcar a thread para parar
            self.threads_ativas[ip].do_run = False
            del self.threads_ativas[ip]
        return True

    def carregar_ips(self):
        with sqlite3.connect('monitor_ip.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT ip, descricao FROM ips")
            for ip, desc in cursor.fetchall():
                self.iniciar_monitoramento(ip, desc)

monitor = MonitorIP()

if __name__ == "__main__":
    # Criar janela com webview
    webview.create_window(
        "Monitor de IPs",
        "templates/index.html",
        js_api=monitor,
        width=1200,
        height=800,
        min_size=(800, 600)
    )
    webview.start() 