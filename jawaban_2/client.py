import socket

def client():
    host = socket.gethostname()
    port = 5000

    client = socket.socket()
    client.connect((host, port))

    message = input(" -> ")

    while message.lower().strip() != 'bye':
        client.send(message.encode())
        data = client.recv(1024).decode()

        print('server: ' + str(data))

        message = input(" -> ")
        
    client.close()


if __name__ == '__main__':
    client()
