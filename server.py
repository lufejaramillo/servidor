import socket
import time

# Servidor

HOST = '192.168.1.7'  # Dirección IP o hostname del servidor
PORT = 65432        # Puerto de escucha (puertos no privilegiados > 1024)

Hora = time.strftime("%H:%M:%S;")
Fecha = time.strftime("%Y/%m/%d")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(Fecha + " " + Hora + " " + "Conexión recibida desde", addr[0])
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
