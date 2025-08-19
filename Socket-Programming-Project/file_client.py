import socket

client = socket.socket()
client.connect(('localhost', 8888))

while True:
    command = input("Enter command (LIST, GET filename, STORE filename, DELETE filename, EXIT): ")
    client.send(command.encode())

    if command.startswith('GET'):
        filename = command.split()[1]
        data = client.recv(100000)
        with open(f'client_files/{filename}', 'wb') as f:
            f.write(data)
        print("File downloaded.")
    elif command.startswith('STORE'):
        filename = command.split()[1]
        with open(f'client_files/{filename}', 'rb') as f:
            data = f.read()
        client.send(data)
        print(client.recv(1024).decode())
    elif command in ['LIST', 'DELETE']:
        print(client.recv(1024).decode())
    elif command == 'EXIT':
        break
client.close()
