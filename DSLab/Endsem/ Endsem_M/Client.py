import socket 

Host = "127.0.0.1"
Port = 12345

s = socket.socket()

numbers = input(str("Enter the numbers:"))

s.connect((Host, Port))
#print(addr[0], "connected")

s.send(numbers.encode())


