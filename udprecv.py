print("udp host ready")

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8',1))
    return s.getsockname()[0]
    

hostip = get_ip()

print("hostip:", hostip)
sock.bind((hostip, 1234))

while True:
    data, addr = sock.recvfrom(1024)
    print("msg:",data)
    sock.sendto("msg ok".encode(), addr)


