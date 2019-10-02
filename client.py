#!/usr/bin/env python3

import socket

HOST = '192.168.1.6'  # Hostname del servidor o dirección de IP
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, World!')
    data = s.recv(1024)

print('Received', repr(data))