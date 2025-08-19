import socket
import threading

def handle_receive(client):
    while True:
        msg = client.recv(1024).decode()
        if msg:
            print("Server:", msg)

def handle_send(client):
    while True:
        msg = input()
        client.send(msg.encode())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5555))

threading.Thread(target=handle_receive, args=(client,), daemon=True).start()
handle_send(client)
