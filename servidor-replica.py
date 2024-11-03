import socket
import time
import random

def replica_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9999))  # IP del servidor maestro

    while True:
        # Simular latencia aleatoria
        time.sleep(random.uniform(0.1, 1.0))  # Retraso aleatorio entre 100ms y 1s

        data = client.recv(1024)
        if not data:
            break

        print(f"Datos replicados (con retraso): {data.decode('utf-8')}")

    client.close()

if __name__ == "__main__":
    replica_server()
