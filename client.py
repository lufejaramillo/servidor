import socket

# Cliente

HOST = '192.168.1.7'  # Hostname del servidor o dirección de IP
PORT = 65432        # Puerto utilizado por el servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, World!')
    data = s.recv(1024)

print('Received', repr(data))