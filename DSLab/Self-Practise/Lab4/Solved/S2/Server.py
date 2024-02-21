import socket
import time

HOST = '127.0.0.1'
PORT = 9999

server=socket.socket()
server.bind((HOST, PORT))
server.listen()

while True:
    conn, addr = server.accept()
    print('Connected by', addr)
    
    currtime=time.ctime(time.time())+"\r\n"
    conn.send(currtime.encode("ascii"))
    conn.close()