import sys
import pygame
import time
from pygame.locals import *

pygame.init()
print("Loading Pong ... ")

width = pygame.display.Info().current_w
height = pygame.display.Info().current_h
print("w",width, " h", height)
size = width, height
background = 0,0,0
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)


mainloop = True
clock = pygame.time.Clock()

ballrect = Rect(width/2, height/2, 16, 16)
computerrect = Rect(width - 20, 0, 20, 120)
playerrect = Rect(0, 0, 20, 120)

normalspeed = 512
speed = [normalspeed,normalspeed]
playerspeed = 0

while mainloop:
    seconds = clock.tick(30) / 1000.0
    
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            mainloop = False
            
        if (event.type == KEYDOWN):
            if (event.key == K_ESCAPE):
                mainloop = False
            if (event.key == K_UP):
                playerspeed = -20
            if (event.key == K_DOWN):
                playerspeed = 20
        if (event.type == KEYUP):
            playerspeed = 0
                
    
    ballrect.x += speed[0] * seconds
    ballrect.y += speed[1] * seconds    
    if ballrect.left < 0 or ballrect.right > width:
        ballrect.x = width / 2
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    
    computerrect.y = ballrect.y
    
    playerrect.y += playerspeed
    
    if computerrect.colliderect(ballrect):
        speed[0] = -speed[0]
    if playerrect.colliderect(ballrect):
        speed[0] = -speed[0]
        
    screen.fill(background)
    pygame.draw.rect(screen, (255,255,255), ballrect)
    pygame.draw.rect(screen, (255,255,255), computerrect)
    pygame.draw.rect(screen, (255,255,255), playerrect)
    pygame.display.update()
    