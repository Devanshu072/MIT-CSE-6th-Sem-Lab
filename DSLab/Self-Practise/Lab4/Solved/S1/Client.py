import socket

HOST = '192.168.1.4'
PORT = 9999

client = socket.socket()
client.connect((HOST, PORT))

data=input("Enter message to send to server : ")
client.send(data.encode())

data=client.recv(1024)
print('Server sent back :', data.decode())

client.close()