import socket

def main():
    host = '127.0.0.1'
    port = 12345

    numbers = [121, 123, 1331, 45654, 789]

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    data = ','.join(map(str, numbers))
    client_socket.send(data.encode())

    response = client_socket.recv(1024).decode()
    print("Response from server:", response)

    client_socket.close()

if __name__ == "__main__":
    main()
