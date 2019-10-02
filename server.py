import socket
import time

HOST = '192.168.1.6'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
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
