
import socket 
 
def send_data_to_master(data): 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client.connect(('192.168.0.11', 9999))  # IP del servidor maestro 
 
    client.send(data.encode('utf-8')) 
    client.close() 
 
if __name__ == "__main__": 
    while True: 
        data = input("Ingresa los datos para enviar al maestro: ") 
        send_data_to_master(data)