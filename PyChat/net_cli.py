import socket

host = ('127.0.0.1', 50007)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 50007))

while True:
    msg = input('Enter:')
    if not msg:
        continue

    if msg == 'exit':
        break

    s.sendall(msg.encode('utf-8'))

s.close()
