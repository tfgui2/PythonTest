from setting import *  # for host
import time
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setblocking(False)


def udpsend(msg):
    sock.sendto(msg, host)
    
def udpbytesend(byte):
    sock.sendto(bytes([byte]), host)

def udpreceive():
    try:
        data,addr =sock.recvfrom(16);
        if data:
            print("received:", data)
            return data
        else:
            print('nonono')
    except:
        pass
    
def main():
    while True:        
        msg = input("input:");
        if msg == "exit" :
            exit()
        udpsend(msg.encode())
        udpreceive()
        time.sleep(0.01)
    
if __name__=='__main__':
    main()