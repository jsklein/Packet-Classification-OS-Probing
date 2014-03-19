import socket



UDP_IP = "1.1.1.1"

UDP_PORT = 5555



sock = socket.socket(socket.AF_INET, # Internet

                     socket.SOCK_DGRAM) # UDP

sock.bind((UDP_IP, UDP_PORT))

i=1

while True:

    data, addr = sock.recvfrom(1024) 

    print str(i)

    i=i+1