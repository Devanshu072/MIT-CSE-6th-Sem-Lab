import socket
HOST = '172.16.58.111'
PORT = 31621
 # Port to listen on (non-privileged ports are > 1023)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
name = input(str("\nEnter your name: "))
print("\nTrying to connect to ", HOST, "(", PORT, ")\n")
s.sendto(b"" , (HOST , PORT))
print("Connected...\n")
s.sendto(name.encode('ascii') , (HOST , PORT))
s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat room\nEnter [e] to exit chat room\n") 
while True:
    message, addr = s.recvfrom(1024) 
    message = message.decode() 	                
    print(s_name, ":", message) 
    message = input(str("Me : "))
    if message == "[e]":
	    message = "Left chat room!"
        s.sendto(message.encode() , (HOST , PORT)) 
        print("\n")
	break
s.sendto(message.encode() , (HOST , PORT))