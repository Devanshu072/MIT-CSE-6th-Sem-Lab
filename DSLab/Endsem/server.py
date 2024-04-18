import socket

Host = "127.0.0.1"
Port = 12345

s = socket.socket()
s.bind((Host, Port))
s.listen()
conn, addr = s.accept()

print("TCP server has started and is ready to receive.")

data_str = conn.recv(1024).decode()  # Receive data as a string
data_list = data_str.split()  # Split the string by spaces

# Convert the list of number strings to a list of integers
data_list = [int(num) for num in data_list]

print("Received data from client:", data_list)

# Calculate the sum of digits for each number
digit_sums = [sum(int(digit) for digit in str(num)) for num in data_list]

print("Sum of digits in the List:")
for num, digit_sum in zip(data_list, digit_sums):
    print(f"{num}: {digit_sum}")

# Calculate the sum of odd and even numbers
even_sum = sum(num for num in data_list if num % 2 == 0)
odd_sum = sum(num for num in data_list if num % 2 != 0)

# Send the sums back to the client
conn.send(f"Even sum: {even_sum}\nOdd sum: {odd_sum}".encode())

conn.close()
s.close()
