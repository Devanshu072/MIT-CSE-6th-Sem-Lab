import socket

Host = "127.0.0.1"
Port = 12345

s = socket.socket()
s.bind((Host, Port))
s.listen()
conn,addr = s.accept()
print(addr[0] ,"hass eneterd the chat room with ", addr[1])

s_name = conn.recv(1024)
s_name  = s_name.decode()
print("naame of the client is ", s_name)

name = input(str("Enter the name:"))
conn.send(name.encode())

while True:
    message = input(str("Me: "))
    if message == '[e]':
        print("Exiting")
        conn.send(message.encode())
        print("/n")
        break
    
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(s_name,":", message)