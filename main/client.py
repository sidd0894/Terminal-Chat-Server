import socket
import threading

SERVER = input('Enter the IPv4 address of server: ')
while True:
    try:
        PORT = int(input('Port number: '))
        break
    except:
        print('Invalid port number.')

ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECTION_MSG = '!DISCONNECT'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

user = ''
while (user == ''):
    user = (input('Enter your name: ')).strip()
    if (user == ''):
        print('Invalid name')
    else:
        break

def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(2048).decode(FORMAT)
            if not data:
                print('[DISCONNECTED] Connection closed by server.')
                break
            print(data)
        except Exception as e:
            print('[DISCONNECTED] Disconnected from server.')
            print(e)
            break

    client_socket.close()
        


def start_client():
    client.connect(ADDR)
    print(f'[CONNECTED] Connected successfully to {ADDR}.\n')

    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    while True:
        try:
            message = (input('')).strip()
            if (message != ''):
                if (message.lower() == '/exit'):
                    client.send(DISCONNECTION_MSG.encode(FORMAT))
                    break
                elif (message.lower() == '/active'):
                    client.send('/active'.encode(FORMAT))
                else:
                    message = f'{user}: {message}'
                    client.send(message.encode(FORMAT))
        except Exception as e:
            print(f'[ERROR] Error occured while sending data to server: {e}')
    client.close()


if __name__ == '__main__':
    print(f'[CONNECTING] Connecting to server {SERVER}...')
    try:
        start_client()
    except KeyboardInterrupt:
        print('[DISCONNECTING] Disconnecting from server...')
        client.close()