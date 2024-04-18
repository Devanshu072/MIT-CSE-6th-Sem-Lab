import socket 

Host = "127.0.0.1"
Port = 12345

s = socket.socket()

name = input(str("Enter your name:"))

s.connect((Host, Port))
print("COnnected..")

s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, " Has entered the chat")

while True:
    message = s.recv(1024)
    message = message.decode()
    print(s_name,":", message)
    message = input(str("me:"))
    if message =="[e]":
        message = "left the chat room"
        s.send(message.encode())
        print("/n")
        break
    
    s.send(message.encode())


