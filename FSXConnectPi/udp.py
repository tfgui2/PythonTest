import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host=('192.168.10.9', 1234)

def udpsend(msg):
    sock.sendto(msg, host)
    
def udpbytesend(byte):
    sock.sendto(bytes([byte]), host)
    
    
def main():
    while True:
        msg = input("input:");
        if msg == "exit" :
            exit()
        udpsend(msg.encode())
        #data, addr = sock.recvfrom(1024)
        #print("reply:", data)

if __name__=='__main__':
    main()