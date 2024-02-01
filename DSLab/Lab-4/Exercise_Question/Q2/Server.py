import socket

HOST = socket.gethostname()
PORT = 31621 # Port to listen on (non-privileged ports are > 1023) 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
s.bind((HOST, PORT)) 
print("\nWaiting for incoming connections...\n")
data,addr = s.recvfrom(1024)
print("Received connection from ", addr[0], "(", addr[1], ")\n") 
s_name, addr = s.recvfrom(1024) 
s_name = s_name.decode()

print(s_name, "has connected to the chat room\nEnter [e] to exit chat room\n") 
name = input(str("Enter your name: "))
s.sendto(name.encode('ascii') , addr)

while True: 
    message = input(str("Me : ")) 
    if message == "[e]": 
        message = "Left chat room!" 
        s.sendto(message.encode() , addr) 
        print("\n")
    break 
s.sendto(message.encode() , addr) 
message, addr = s.recvfrom(1024) 
message = message.decode() 
print(s_name, ":", message) 