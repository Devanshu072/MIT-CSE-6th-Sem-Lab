import socket 

Host = "127.0.0.1"
Port = 12345

s = socket.socket()
s.bind((Host, Port))
s.listen()
conn,addr = s.accept()

print("TCP server ahs started and is ready to receive")

numbers = conn.recv(1024)
numbers = numbers.decode()
number_list = numbers.split()
numbers_str = ','.join(number_list)
numbers_str = [int(num) for num in number_list]

print("Received data from client" ,numbers_str)

