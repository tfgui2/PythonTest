#main ui
import pygame
import ui_button
pygame.init()
pygame.font.init()
pygame.display.set_caption('FSXConnectPI')
screen = pygame.display.set_mode((720,480), pygame.FULLSCREEN)
font1 = pygame.font.Font('freesansbold.ttf', 16)
font2 = pygame.font.Font('freesansbold.ttf', 30)
green = (0, 128, 64) 
blue = (0, 0, 128)
btnmode=ui_button.ModeButton((35,50))
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

class MainUI:
    def __init__(self):
        self.running=True
        ### resource
        self.background = pygame.image.load('background.bmp')
        ### buttons
        self.buttons = []
        self.makebuttons()
        # rendering start
        screen.blit(self.background, (0,0))
        text = font1.render('FSXConnectPI', True, green, blue)
        screen.blit(text, (20,15))
        
        
    def makebuttons(self):
        x=50
        dx=130
        y=210
        for i in range(1,6):
            self.addbutton(i, (x,y), False)
            x +=dx
            
        x=50
        dx=130
        y=340
        for i in range(6,11):
            self.addbutton(i, (x,y), True)
            x +=dx
        
        
    def addbutton(self, id, pos, toggle):
        if toggle:
            btn=ui_button.ToggleButton(id, pos)
        else:
            btn=ui_button.Button(id, pos)
        self.buttons.append(btn)

    def getevent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.close()
                return True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = event.pos
                for bt in self.buttons:
                    if bt.check(mousepos):
                        print (bt.id)
                        return True
                if btnmode.check(mousepos):
                    print('mode')
                    return True
        return False
    
    def displaytext(self):
        x=230
        line1 = 60
        line2 = 100
        text = font2.render('hello world', True, blue)
        screen.blit(text, (x,line1))
        screen.blit(font2.render('hello world', True, blue), (x,line2))
        
        
    def render(self):
        # rendering start
        #screen.blit(self.background, (0,0))
        btnmode.display(screen)
        
        # display text
        self.displaytext()
        
        # display buttons
        for bt in self.buttons:
            bt.display(screen)

        pygame.display.update()
        
    def close(self):
        pygame.quit()
        
        
if __name__=='__main__':
    gui=MainUI()
    while True:
        gui.getevent()
        gui.render()
