import socket

Host = "127.0.0.1"
Port = 12345

s = socket.socket()

numbers = input("Input integers with space in between: ")  # Input numbers with spaces

s.connect((Host, Port))
print("Connected to server.")

s.send(numbers.encode())

data = s.recv(1024).decode()
print("Received from server.")
print(data)

s.close()
