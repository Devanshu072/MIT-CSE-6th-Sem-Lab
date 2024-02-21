import socket
HOST = '127.0.0.1' 
PORT = 9999
server_address=(HOST,PORT)

client = socket.socket()

name = input("Enter your name: ")
print("\nConnecting to host...")

if client.connect(server_address):
    print("Connected...\n")

client.send(name.encode())
s_name = client.recv(1024).decode()

print(s_name, "has joined the chat room\nEnter [q] to exit chat room\n")

while True:
    message = s.recv(1024)
    message = message.decode()
    print(s_name, ":", message)
    message = input(str("Me : "))
    if message == "[e]":
        message = "Left chat room!"
        s.send(message.encode())
        print("\n")
    break
s.send(message.encode())