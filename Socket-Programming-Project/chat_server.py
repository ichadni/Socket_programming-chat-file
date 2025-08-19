import socket
import threading

def handle_receive(conn):
    while True:
        msg = conn.recv(1024).decode()
        if msg:
            print("Client:", msg)

def handle_send(conn):
    while True:
        msg = input()
        conn.send(msg.encode())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5555))
server.listen(1)
print("Waiting for connection...")
conn, addr = server.accept()
print("Connected with", addr)

threading.Thread(target=handle_receive, args=(conn,), daemon=True).start()
handle_send(conn)
