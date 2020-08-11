import pygame
import socket

print('udp test')

udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

hostip = '192.168.10.9'
port = 1234

while True:
    msg = input('input: ')
    if msg == 'exit':
        exit()
    
    udpsock.sendto(msg.encode(), (hostip, port))
    