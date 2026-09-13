# TCP Client-Server Communication System

<p align="center">
  A Python-based TCP client-server system supporting real-time two-way chat and remote file management.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Networking-TCP-orange?style=for-the-badge" alt="TCP">
  <img src="https://img.shields.io/badge/Socket-Programming-green?style=for-the-badge" alt="Socket Programming">
  <img src="https://img.shields.io/badge/Multithreading-Supported-purple?style=for-the-badge" alt="Multithreading">
</p>

---

## 📌 Overview

This project demonstrates practical **TCP socket programming in Python** through two client-server applications.

### Part 1 — Real-Time Chat Application

A two-person client-server chat system where both users can communicate through TCP sockets.

The application uses **multithreading** so that a user can:

* Send a message without waiting for a reply
* Send multiple messages continuously
* Receive incoming messages while typing or sending messages
* Communicate in both directions in real time

### Part 2 — Client-Server File Management System

A TCP-based file server and client that allows the client to remotely manage files stored on the server.

The client can:

* List files available on the server
* Store/upload a file to the server
* Download/get a file from the server
* Delete a file from the server
* Exit the connection

---

# 🚀 Project Parts

```text
              TCP Client-Server System
                       │
             ┌─────────┴─────────┐
             │                   │
             ▼                   ▼
      Part 1: Chat        Part 2: File Management
             │                   │
             ▼                   ▼
       Two-way Chat       LIST / STORE / GET
       Send Multiple       DELETE / EXIT
       Messages
```

---

# 💬 Part 1: TCP Chat Application

## Features

* Two-person client-server communication
* Real-time bidirectional messaging
* Send multiple messages continuously
* No need to wait for the other person's reply
* TCP-based reliable communication
* Multithreaded message receiving
* Command-line interface
* Localhost communication
* Continuous send and receive operations

---

## 🏗️ Chat Architecture

```text
                 TCP Connection
        ┌──────────────────────────┐
        │                          │
        ▼                          ▼
┌───────────────┐            ┌───────────────┐
│     Person 1  │◄──────────►│    Person 2   │
│    (Client)   │     TCP    │    (Server)   │
│               │            │               │
│ Port: 5555    │            │ Port: 5555    │
└───────┬───────┘            └───────┬───────┘
        │                            │
        ▼                            ▼
 Receive Thread                Receive Thread
        │                            │
        ▼                            ▼
     Messages                    Messages
```

---

## 🔄 Multiple Message Communication

A key feature of this application is that a person does **not need to wait for a reply before sending another message**.

For example:

```text
Person 1                          Person 2
   │                                  │
   │──── Hello ──────────────────────►│
   │──── How are you? ───────────────►│
   │──── Are you available? ─────────►│
   │──── I need to discuss something ►│
   │                                  │
   │◄──────────── Hi! ────────────────│
   │◄──────────── I'm fine. ──────────│
```

This is possible because the receiving operation runs in a separate thread.

---

## 🧵 Multithreading

The application separates **sending and receiving operations**.

```text
                  User
                   │
             ┌─────┴─────┐
             ▼           ▼
          Sending     Receiving
             │           │
          input()      recv()
             │           │
             ▼           ▼
          TCP Socket ←→ TCP Socket
```

The receive thread continuously waits for incoming messages while the main program remains available for sending messages.

Example:

```python
threading.Thread(
    target=handle_receive,
    args=(client,),
    daemon=True
).start()
```

---

## 🔄 Chat Communication Flow

```text
Client                                  Server
  │                                       │
  │──── Connection Request ─────────────►│
  │                                       │
  │◄──── Connection Accepted ────────────│
  │                                       │
  │──── Message 1 ──────────────────────►│
  │──── Message 2 ──────────────────────►│
  │──── Message 3 ──────────────────────►│
  │                                       │
  │◄──── Reply 1 ────────────────────────│
  │◄──── Reply 2 ────────────────────────│
  │                                       │
```

---

# 📁 Part 2: TCP File Management System

## Features

The second part implements a **file server and client** using TCP socket programming.

The client can perform four major file-management operations:

| Command           | Function                          |
| ----------------- | --------------------------------- |
| `LIST`            | View files stored on the server   |
| `STORE filename`  | Upload/store a file on the server |
| `GET filename`    | Download a file from the server   |
| `DELETE filename` | Delete a file from the server     |
| `EXIT`            | Close the connection              |

---

## 🏗️ File Management Architecture

```text
                  TCP Connection
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
   ┌──────────────┐          ┌──────────────┐
   │    Client    │◄────────►│    Server    │
   │              │   TCP    │              │
   │ Port: 8888   │          │ Port: 8888   │
   └──────┬───────┘          └──────┬───────┘
          │                         │
          ▼                         ▼
   client_files/             server_files/
```

---

## 🔄 File Management Workflow

```text
                    Client
                       │
                       ▼
                 Enter Command
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
        LIST         STORE         GET
          │            │            │
          ▼            ▼            ▼
       Request      Upload        Download
          │            │            │
          └────────────┼────────────┘
                       │
                       ▼
                     Server
                       │
                       ▼
                server_files/
                       │
                       ▼
                  File Operation
```

---

## 📋 LIST

The client can request a list of files stored on the server.

```text
Client:
LIST

Server:
file1.txt
image.jpg
document.pdf
```

The server reads the contents of the `server_files` directory and sends the filenames back to the client.

---

## ⬆️ STORE

The `STORE` command allows the client to send a file to the server.

```text
Client:
STORE example.txt
       │
       │ File Data
       ▼
Server
       │
       ▼
server_files/example.txt
```

After storing the file, the server responds:

```text
FILE STORED
```

---

## ⬇️ GET / Download

The client can request a file from the server.

```text
Client:
GET example.txt
       │
       ▼
     Server
       │
       ▼
server_files/example.txt
       │
       │ File Data
       ▼
     Client
       │
       ▼
client_files/example.txt
```

After receiving the file, the client displays:

```text
File downloaded.
```

---

## 🗑️ DELETE

The client can request the server to delete a stored file.

```text
Client
   │
   │ DELETE example.txt
   ▼
Server
   │
   ▼
Remove file
   │
   ▼
FILE DELETED
```

If the requested file does not exist:

```text
FILE NOT FOUND
```

---

# 🛠️ Technology Stack

| Technology       | Purpose                           |
| ---------------- | --------------------------------- |
| **Python 3.x**   | Application development           |
| **Socket**       | TCP network communication         |
| **TCP**          | Reliable data transmission        |
| **Threading**    | Concurrent chat sending/receiving |
| **OS Module**    | Server-side file management       |
| **Command Line** | User interaction                  |

No external Python packages are required.

---

# 📂 Project Structure

```text
TCP-Client-Server/
│
├── Chat/
│   ├── client.py
│   └── server.py
│
├── File_Management/
│   ├── client.py
│   ├── server.py
│   ├── client_files/
│   └── server_files/
│
└── README.md
```

> Adjust the folder names above if your actual GitHub repository uses a different structure.

---

# ⚙️ Part 1 Setup — Chat

## 1. Start the Server

Open a terminal and run:

```bash
python server.py
```

Output:

```text
Waiting for connection...
```

## 2. Start the Client

Open another terminal:

```bash
python client.py
```

The client connects to:

```text
localhost:5555
```

---

# ⚙️ Part 2 Setup — File Management

## 1. Create Required Folders

Inside the project:

```text
client_files/
server_files/
```

Place files you want to upload inside:

```text
client_files/
```

## 2. Start the File Server

```bash
python server.py
```

The server listens on:

```text
localhost:8888
```

## 3. Start the File Client

Open another terminal:

```bash
python client.py
```

---

# 💻 File Commands

```text
LIST
```

Displays files stored on the server.

```text
STORE filename
```

Uploads a file from `client_files/` to `server_files/`.

```text
GET filename
```

Downloads a file from `server_files/` to `client_files/`.

```text
DELETE filename
```

Deletes a file from the server.

```text
EXIT
```

Terminates the client-server session.

---

# 🔌 Important Socket Operations

| Operation   | Purpose                         |
| ----------- | ------------------------------- |
| `socket()`  | Creates a network socket        |
| `bind()`    | Assigns server address and port |
| `listen()`  | Waits for client connections    |
| `accept()`  | Accepts an incoming connection  |
| `connect()` | Connects the client to server   |
| `send()`    | Sends data                      |
| `recv()`    | Receives data                   |
| `close()`   | Closes the connection           |

---

# 🧠 Networking Concepts Demonstrated

This project provides practical experience with:

* Client-server architecture
* TCP/IP communication
* Socket programming
* IP addresses
* Port numbers
* TCP connections
* `bind()`
* `listen()`
* `accept()`
* `connect()`
* `send()`
* `recv()`
* Multithreading
* Bidirectional communication
* File transfer over TCP
* Remote file management

---

# 🔐 Current System Scope

The current implementation is designed as a **learning project for TCP socket programming**.

It currently uses:

```text
Chat       → localhost:5555
File       → localhost:8888
Clients    → One connected client/server pair
Interface  → Command Line
```

The implementation demonstrates the core networking concepts without additional authentication, encryption, or multi-client management.

---

# 🚀 Future Improvements

### Chat Application

* Multiple simultaneous users
* Usernames and authentication
* Private messaging
* Message timestamps
* Chat history
* GUI interface
* Encrypted communication
* Online/offline status

### File Management System

* Multiple simultaneous clients
* File size handling using chunked transfer
* File metadata
* Authentication and authorization
* Secure file transfer
* Progress indicators
* GUI interface
* Directory management
* File search
* Access permissions

---

# 🎓 Learning Outcomes

This project demonstrates how Python can be used to build practical network applications using low-level TCP socket programming.

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
Real-Time Chat
   ↓
File Transfer
   ↓
Remote File Management
```

---

# 👩‍💻 Author

**Israt Jahan Chadni**

GitHub: @ichadni

---

<p align="center">
  ⭐ If you found this project useful, consider giving the repository a star.
</p>
