#main ui
import pygame
import ui_button
pygame.init()
pygame.font.init()
pygame.display.set_caption('FSXConnectPI')
screen = pygame.display.set_mode((720,480))
font = pygame.font.Font('freesansbold.ttf', 16)
green = (0, 128, 64) 
blue = (0, 0, 128)

class MainUI:
    def __init__(self):
        ### resource
        self.background = pygame.image.load('background.bmp')
        ### buttons
        self.buttons = []
        btn1 = ui_button.Button(1, (10,100))
        self.buttons.append(btn1)
        btn2 = ui_button.ToggleButton(2, (200,100))
        self.buttons.append(btn2)
        self.running=True

    def getevent(self):
        for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.running = False
            return True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = event.pos
            for bt in self.buttons:
                if bt.check(mousepos):
                    print (bt.id)
                    return True
        return False
        
    def render(self):
        # rendering start
        screen.blit(background, (0,0))
        
        # display text
        text = font.render('FSXConnect', True, green, blue)
        screen.blit(text, (10,10))
        
        # display buttons
        for bt in buttons:
            bt.display(screen)

        pygame.display.update()
        
    def close(self):
        pygame.quit()
        
        
