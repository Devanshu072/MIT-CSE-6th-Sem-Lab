import socket

Host = "127.0.0.1"
Port = 12346

s = socket.socket()
name = input(str("Enter the name:"))

s.connect((Host, Port))
print("connecting..... /n Connected..")

s.send = name.encode()
s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, "Has connected")

while True:
    message = s.recv(1024)
    message = message.decode()
    print(s_name,":", message )
    message = input(str("Me:"))
    if message == "[e]":
        message == "Exit chat"
        s.send = message.encode()
        print("/n")
        break
    s.send = message.encode()
        
    


