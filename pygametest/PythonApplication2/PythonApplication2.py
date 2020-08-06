import pygame

pygame.init()


screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('FSXConnectPI')
clock = pygame.time.Clock()

background = pygame.image.load('background.bmp')
buttonoff = pygame.image.load('button_off.bmp')
buttonon = pygame.image.load('button_on.bmp')
buttonpos = (100, 100)

running = True
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = event.pos
            rect = buttonoff.get_rect();
            rect.left = 100
            rect.top = 100
            if rect.collidepoint(mousepos):
                print(event)
            

    screen.blit(background, (0,0))
    screen.blit(buttonoff, buttonpos)

    pygame.display.update()

pygame.quit()
