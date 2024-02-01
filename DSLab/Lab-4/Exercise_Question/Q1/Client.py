import socket
# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
# get local machine name
udp_host = socket.gethostname()
udp_port = 9991

#Send some message so the server gets client address
msg = 'hi'
s.sendto(msg.encode(),(udp_host,udp_port))

# Receive no more than 1024 bytes
tm = s.recv(1024)
print(' Current time from Sever :', tm.decode())
s.close()
