class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.clock = 0  # Reloj lógico para la consistencia causal
        self.messages = []  # Mensajes recibidos

    def send_message(self, recipient, message):
        self.clock += 1  # Incrementar el reloj antes de enviar
        # Crear el mensaje con el reloj y el contenido
        msg = (self.clock, message)  # (timestamp, message)
        print(f"Node {self.node_id} sending: {msg}")
        recipient.receive_message(msg)

    def receive_message(self, msg):
        timestamp, message = msg
        # Actualizar el reloj lógico
        self.clock = max(self.clock, timestamp) + 1
        self.messages.append((timestamp, message))
        print(f"Node {self.node_id} received: {msg}")

# Ejemplo de uso
node_A = Node('A')
node_B = Node('B')

# Node A envía un mensaje a Node B
node_A.send_message(node_B, "Hello B!")  # A: 1

# Node B responde a Node A
node_B.send_message(node_A, "Hello A!")  # B: 2

# Mensajes recibidos en cada nodo
print(f"Node A messages: {node_A.messages}")
print(f"Node B messages: {node_B.messages}")
