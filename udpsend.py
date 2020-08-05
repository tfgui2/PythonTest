print("udp test")

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

hostip = input('hostip:')
print("hostip:",hostip)
check = input('is ok? (y/n)')
if check == 'n':
    exit()


while True:
    msg = input("input:");
    if msg == "exit" :
        exit()
    sock.sendto(msg.encode(), (hostip, 1234))
    data, addr = sock.recvfrom(1024)
    print("reply:", data)
