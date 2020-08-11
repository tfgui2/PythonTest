print("udp host ready")
import time
import random

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setblocking(False)

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8',1))
    return s.getsockname()[0]
    

hostip = get_ip()

print("hostip:", hostip)
sock.bind((hostip, 1234))

count=0
remote=None
while True:
    time.sleep(0.5)
    count+=1
    if remote:
        r=random.randrange(5)
        print('random',r)
        if r==1:
            sock.sendto(("%dmsg ok"%count).encode(), remote)
        
    try:
        data, addr = sock.recvfrom(1024)
        if data:
            remote=addr
            print("msg:",data)
        
        else:
            print('no data')
        
    except:
        pass


