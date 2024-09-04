import socket
import threading

HOSTNAME = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (HOSTNAME, PORT)
FORMAT = 'utf-8'
DISCONNECTION_MSG = '!DISCONNECT'

clients = []
clients_lock = threading.Lock()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f'New connection from {addr}')
    try:
        while True:
                data = conn.recv(2048).decode(FORMAT)
                if not data:
                    break
                elif (data == DISCONNECTION_MSG):
                    break
                elif (data == '/active'):
                    conn.send(f'ACTIVE - {len(clients)}'.encode(FORMAT))
                else:
                    try:
                        with clients_lock:
                            for client in clients:
                                if (client != conn):
                                    client.send(data.encode(FORMAT))
                    except Exception as e:
                        print(f'Error sending messages to client {addr}: {e}')
    
    finally:
        try:
            with clients_lock:
                clients.remove(conn)
            conn.close()
        except Exception as e:
            print(f'Error disconnecting client {addr}: {e}')

def start_server():
    server.listen()
    print(f'Server started {ADDR}...')

    while True:
        try:
            conn, addr = server.accept()
            with clients_lock:
                clients.append(conn)
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
        except Exception as e:
            print(f'Error accepting connection from client {addr}: {e}')

if __name__ == '__main__':
    try:
        start_server()
    except KeyboardInterrupt:
        print('Shutting down server...')
        server.close()