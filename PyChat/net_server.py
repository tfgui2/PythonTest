import sys
import threading
import socket
import time

connlist = []

class ClientConn(threading.Thread):
    def set(self, conn):
        self.conn = conn

    def run(self):
        while True:
            data = self.conn.recv(1024)
            if not data:
                break

            print("Receive " + data.decode('utf-8'))

    def stop(self):
        print("Stop")
        self.conn.close()
        

class Acceptor(threading.Thread):
    host = ('127.0.0.1', 50007)
    isStop = False
    
    def run(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(self.host)
        self.s.listen(1)

        while True:
            if self.isStop:
                break
            
            conn, addr = self.s.accept()

            print("Connect by " + str(addr))

            c = ClientConn()
            c.set(conn)
            c.start()
            connlist.append(c)

        self.s.close()
        print("Acceptor stop")

    def stop(self):
        self.isStop = True;
        socket.socket(socket.AF_INET, socket.SOCK_STREAM)


acceptor = Acceptor()
acceptor.start()

while True:
    com = input('>')
    if not com:
        continue

    if com == 'exit':
        acceptor.stop()
        for cli in connlist:
            cli.stop()

        print("Exit")
        break

