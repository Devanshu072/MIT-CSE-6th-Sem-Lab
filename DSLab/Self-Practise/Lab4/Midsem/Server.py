import socket

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def main():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Server listening on port:", port)

    while True:
        conn, addr = server_socket.accept()
        print("Connection from:", addr)

        data = conn.recv(1024).decode()
        numbers = data.split(',')

        palindrome = []
        non_palindrome = []

        for num in numbers:
            num = int(num.strip())
            if is_palindrome(num):
                palindrome.append(num)
            else:
                non_palindrome.append(num)

        conn.send(f"Palindrome numbers: {palindrome}\nNon-palindrome numbers: {non_palindrome}".encode())

        conn.close()

if __name__ == "__main__":
    main()
