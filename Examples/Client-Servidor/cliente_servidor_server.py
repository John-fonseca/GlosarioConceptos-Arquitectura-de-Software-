import socket

# Configuración del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 65432))  # Host y puerto
server_socket.listen()

print('Servidor a la espera de conexiones...')

conn, addr = server_socket.accept()  # Aceptar una conexión
with conn:
    print(f'Conectado por {addr}')
    while True:
        data = conn.recv(1024)  # Recibir datos
        if not data:
            break
        print(f'Datos recibidos: {data.decode()}')
        conn.sendall(b'Respuesta del servidor')  # Enviar respuesta
