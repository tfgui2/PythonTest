import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

def main():
    while True:
        for event_var in pygame.event.get():
            if event_var.type == QUIT:
                pygame.quit()
                return

            elif event_var.type == MOUSEBUTTONDOWN:
                print(event_var)

        clock.tick(60)


main()