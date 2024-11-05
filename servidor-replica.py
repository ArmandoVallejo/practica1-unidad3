
import socket 
 
def replica_server(): 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client.connect(('192.168.223.204', 9999))  # IP del servidor maestro 
 
    while True: 
        data = client.recv(1024) 
        if not data: 
            break 
         
        print(f"Datos replicados: {data.decode('utf-8')}") 
 
    client.close() 
 
if __name__ == "__main__": 
    replica_server()