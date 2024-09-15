import socket

# Configuración del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 65432))  # Conectar al servidor

client_socket.sendall(b'Hola, servidor')  # Enviar mensaje
data = client_socket.recv(1024)  # Recibir respuesta
print(f'Datos recibidos del servidor: {data.decode()}')

client_socket.close()  # Cerrar conexión
