import socket
import os

server = socket.socket()
server.bind(('localhost', 8888))
server.listen(1)
print("Waiting for client...")
conn, addr = server.accept()
print("Connected with", addr)

while True:
    command = conn.recv(1024).decode()
    if command == 'LIST':
        files = os.listdir('server_files')
        conn.send('\n'.join(files).encode())
    elif command.startswith('GET'):
        filename = command.split()[1]
        try:
            with open(f'server_files/{filename}', 'rb') as f:
                data = f.read()
            conn.send(data)
        except FileNotFoundError:
            conn.send(b'FILE NOT FOUND')
    elif command.startswith('DELETE'):
        filename = command.split()[1]
        try:
            os.remove(f'server_files/{filename}')
            conn.send(b'FILE DELETED')
        except FileNotFoundError:
            conn.send(b'FILE NOT FOUND')
    elif command.startswith('STORE'):
        filename = command.split()[1]
        data = conn.recv(100000)
        with open(f'server_files/{filename}', 'wb') as f:
            f.write(data)
        conn.send(b'FILE STORED')
    elif command == 'EXIT':
        break
conn.close()
