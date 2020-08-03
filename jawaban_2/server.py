import socket
import datetime

def server():
    counter = 0
    date = datetime.datetime.now()
    host = socket.gethostname()
    port = 5000

    server = socket.socket()
    server.bind((host,port))
    server.listen(2)
    conn, address = server.accept()
    print("connect : ", str(address))

    while True:
        counter = counter + 1
        data = conn.recv(1024).decode()
        if not data:
            break
        print("client : "+ str(data))
        log = "[" + str(date) + "] Success : POST " + str(address) + "counter : " + str(counter) + ", " + str(data) + "\n"
        data = input(' -> ')
        
        file = open("server.log", "a")
        file.write(log)
        
        conn.send(data.encode())
    conn.close()

if __name__ == '__main__':
    server()
