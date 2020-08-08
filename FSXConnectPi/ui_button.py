import pygame

buttonon = pygame.image.load('button_on.bmp')
buttonoff = pygame.image.load('button_off.bmp')
buttonmodeon=pygame.image.load('button_mode_on.bmp')
buttonmodeoff=pygame.image.load('button_mode_off.bmp')
green = (0, 128, 64) 
blue = (0, 0, 128)

pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 24) 


class Button:
    """description of class"""
    def __init__(self, id, pos):
        rect = buttonon.get_rect()
        rect.left = pos[0]
        rect.top = pos[1]
        self.rect = rect
        self.id = id
        self.setlabel('btn'+str(self.id))
    
    def check(self, point):
        if self.rect.collidepoint(point):
            return True
        return False
    
    def pos(self):
        return (self.rect.left, self.rect.top)

    def display(self, surface):
        surface.blit(buttonoff, self.pos())
        surface.blit(self.text, self.textrect)
     
    def setlabel(self, label):
        self.text = font.render(label, True, green)
        self.textrect = self.text.get_rect()
        self.textrect.center = (self.rect.width // 2, self.rect.height // 2)
        self.textrect.left += self.rect.left
        self.textrect.top += self.rect.top
        

class ToggleButton(Button):
    def __init__(self, id, pos):
        Button.__init__(self, id, pos)
        self.on = False
        self.toggleenable=False
        
    def settoggleenable(self, toggleenable):
        self.toggleenable=toggleenable

    def check(self, point):
        if Button.check(self, point):
            if self.toggleenable:
                self.on = not self.on
            return True
        return False

    def display(self, surface):
        if self.on:
            surface.blit(buttonon, self.pos())
        else:
            surface.blit(buttonoff, self.pos())
        surface.blit(self.text, self.textrect)


class ModeButton(ToggleButton):
    def __init__(self, pos):
        ToggleButton.__init__(self,0,pos)
        self.toggleenable=True

    def display(self, surface):
        if self.on:
            surface.blit(buttonmodeon, self.pos())
        else:
            surface.blit(buttonmodeoff, self.pos())
        
