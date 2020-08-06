
import pygame
import Button

### init
pygame.init()
# screen = pygame.display.set_mode((640,480), pygame.FULLSCREEN)
screen = pygame.display.set_mode((720,480))
pygame.display.set_caption('FSXConnectPI')
clock = pygame.time.Clock()

### resource
background = pygame.image.load('background.bmp')
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 16) 
green = (0, 128, 64) 
blue = (0, 0, 128)

### buttons
buttons = []
btn1 = Button.Button(1, (10,100))
buttons.append(btn1)
btn2 = Button.ToggleButton(2, (200,100))
buttons.append(btn2)


running = True
while running:
    #dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = event.pos
            for bt in buttons:
                if bt.check(mousepos):
                    print(bt.id)

    # rendering start
    screen.blit(background, (0,0))
    
    # display text
    text = font.render('FSXConnect', True, green, blue)
    screen.blit(text, (10,10))
    
    # display buttons
    for bt in buttons:
        bt.display(screen)

    pygame.display.update()

pygame.quit()
