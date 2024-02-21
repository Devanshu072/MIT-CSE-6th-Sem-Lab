import socket

HOST = '127.0.0.1'
PORT = 9999

client = socket.socket()
client.connect((HOST, PORT))

time=client.recv(1024)
print('Server sent back time :', time.decode())

client.close()