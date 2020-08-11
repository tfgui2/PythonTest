print("udp test")
import time
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setblocking(False)

hostip = input('hostip:')
print("hostip:",hostip)
check = input('is ok? (y/n)')
if check == 'n':
    exit()

count=0
while True:
    count+=1
    time.sleep(0.5)
    msg = 'test%d'%count
    if msg == "exit" :
        exit()
    
    sock.sendto(msg.encode(), (hostip, 1234))
    try:
        data, addr = sock.recvfrom(1024)
        print("reply:", data)
    except:
        pass
