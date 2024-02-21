import socket

HOST = '192.168.1.4'
PORT = 9999

server=socket.socket()
server.bind((HOST, PORT))
server.listen()

while True:
    conn, addr = server.accept()
    print('Connected by', addr)
    
    data = conn.recv(1024)
    if data:
        print("Client says : ",data.decode())
    if not data:
        break
    conn.send(bytes(data))
server.close()