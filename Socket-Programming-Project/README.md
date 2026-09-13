# Python TCP Client-Server Chat Application

<p align="center">
  A real-time client-server chat application built using Python socket programming and multithreading.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Networking-TCP-orange?style=for-the-badge" alt="TCP">
  <img src="https://img.shields.io/badge/Socket-Programming-green?style=for-the-badge" alt="Socket Programming">
  <img src="https://img.shields.io/badge/Multithreading-Supported-purple?style=for-the-badge" alt="Multithreading">
</p>

---

## Overview

This project implements a **real-time TCP client-server chat application** using Python's built-in `socket` and `threading` modules.

The server listens for an incoming client connection, while the client connects to the server using a TCP socket. Once connected, both sides can independently send and receive messages.

Multithreading is used to allow message receiving and sending to occur simultaneously.

---

## Features

* Real-time client-server communication
* TCP-based reliable communication
* Bidirectional messaging
* Concurrent message sending and receiving
* Multithreaded architecture
* Simple command-line interface
* Localhost-based communication for testing
* Graceful connection termination

---

## Technology Stack

| Technology       | Purpose                            |
| ---------------- | ---------------------------------- |
| **Python**       | Application development            |
| **Socket**       | Network communication              |
| **TCP**          | Reliable transport protocol        |
| **Threading**    | Concurrent send/receive operations |
| **Command Line** | User interaction                   |

---

## Architecture

```text
                 TCP Connection
        ┌──────────────────────────┐
        │                          │
        ▼                          ▼
┌───────────────┐            ┌───────────────┐
│     Client    │◄───────────►│     Server    │
│               │    TCP      │               │
│ Port: 5555    │             │ Port: 5555    │
└───────┬───────┘            └───────┬───────┘
        │                            │
        ▼                            ▼
┌───────────────┐            ┌───────────────┐
│ Receive Thread│            │ Receive Thread│
└───────────────┘            └───────────────┘
        │                            │
        ▼                            ▼
     Messages                    Messages
```

---

## How It Works

### Server

The server:

1. Creates a TCP socket.
2. Binds it to `localhost:5555`.
3. Starts listening for connections.
4. Accepts a client connection.
5. Creates a receiving thread.
6. Continuously sends messages through the main thread.

```python
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5555))
server.listen(1)
```

### Client

The client:

1. Creates a TCP socket.
2. Connects to the server.
3. Starts a receiving thread.
4. Uses the main thread to send messages.

```python
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5555))
```

---

## Multithreading

The application uses separate threads for receiving messages.

```python
threading.Thread(
    target=handle_receive,
    args=(client,),
    daemon=True
).start()
```

This allows the application to:

```text
             Application
                  │
          ┌───────┴───────┐
          ▼               ▼
       Receive           Send
       Thread            Thread
          │               │
          ▼               ▼
      recv()            input()
          │               │
          └───────┬───────┘
                  ▼
              TCP Socket
```

Without multithreading, the program could become blocked while waiting for either input from the user or incoming network data.

---

## Communication Flow

```text
Client                          Server
  │                               │
  │────── Connection Request ────►│
  │                               │
  │◄──── Connection Accepted ─────│
  │                               │
  │──────── "Hello" ─────────────►│
  │                               │
  │◄──────── "Hi" ────────────────│
  │                               │
  │──────── "How are you?" ─────►│
  │                               │
  │◄──────── "I'm fine" ─────────│
  │                               │
```

---

## Project Structure

```text
TCP-Chat/
│
├── client.py
├── server.py
└── README.md
```

---

## Requirements

* Python 3.x
* Standard Python libraries

  * `socket`
  * `threading`

No external packages are required.

---

## Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
```

### 2. Navigate to the Project

```bash
cd TCP-Chat
```

### 3. Start the Server

Open one terminal and run:

```bash
python server.py
```

The server will display:

```text
Waiting for connection...
```

### 4. Start the Client

Open another terminal and run:

```bash
python client.py
```

The client will connect to the server.

---

## Example

### Server

```text
Waiting for connection...
Connected with ('127.0.0.1', 54321)

Client: Hello Server
Server: Hello Client
```

### Client

```text
Server: Hello Client
Hello Server
```

---

## Networking Concepts Demonstrated

This project provides practical implementation of:

* Client-server architecture
* TCP communication
* IP addresses
* Port numbers
* Socket creation
* Socket binding
* Listening and accepting connections
* Network data transmission
* `send()` and `recv()`
* Multithreading
* Concurrent communication
* Network connection management

---

## Key Socket Operations

| Operation   | Purpose                                        |
| ----------- | ---------------------------------------------- |
| `socket()`  | Creates a network socket                       |
| `bind()`    | Associates the server with an address and port |
| `listen()`  | Waits for incoming connections                 |
| `accept()`  | Accepts a client connection                    |
| `connect()` | Connects the client to the server              |
| `send()`    | Sends data                                     |
| `recv()`    | Receives data                                  |
| `close()`   | Closes the connection                          |

---

## Future Improvements

Possible enhancements include:

* Multiple simultaneous clients
* Usernames and authentication
* Private messaging
* Chat history
* Message timestamps
* GUI using Tkinter or PyQt
* Encrypted communication
* File sharing
* Online/offline user status
* Server-side client management

---

## Learning Outcomes

This project demonstrates how Python can be used to build a basic **networked application** using low-level socket programming.

```text
Python
   ↓
Socket Programming
   ↓
TCP Communication
   ↓
Client-Server Architecture
   ↓
Multithreading
   ↓
Real-Time Communication
```

---

## Author

**Israt Jahan Chadni**

GitHub: [@ichadni](https://github.com/ichadni)

---

<p align="center">
  ⭐ If you found this project useful, consider giving the repository a star.
</p>
