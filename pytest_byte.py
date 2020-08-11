import pygame
import socket
import time

print('udp test')
pygame.init()
screen_size = [400, 300]
pygame.display.set_mode(screen_size)
pygame.display.set_caption('FSXConnectPI')
clock = pygame.time.Clock()

udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

hostip = '192.168.10.9'
port = 1234

while True:
    test = 2
    msg = bytes([test])
    udpsock.sendto(msg, (hostip, port))
    time.sleep(2)
    