import pygame

buttonon = pygame.image.load('button_on.bmp')
buttonoff = pygame.image.load('button_off.bmp')
green = (0, 128, 64) 
blue = (0, 0, 128)

pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 16) 


class Button:
    """description of class"""
    def __init__(self, id, pos):
        rect = buttonon.get_rect()
        rect.left = pos[0]
        rect.top = pos[1]
        self.rect = rect
        self.id = id
        self.text = font.render('button'+str(self.id), True, green)
        self.textrect = self.text.get_rect()
        self.textrect.center = (self.rect.width // 2, self.rect.height // 2)
        self.textrect.left += self.rect.left
        self.textrect.top += self.rect.top

    
    def check(self, point):
        if self.rect.collidepoint(point):
            return True
        return False
    
    def pos(self):
        return (self.rect.left, self.rect.top)

    def display(self, surface):
        surface.blit(buttonoff, self.pos())
        surface.blit(self.text, self.textrect)
        

class ToggleButton(Button):
    def __init__(self, id, pos):
        Button.__init__(self, id, pos)
        self.on = False

    def check(self, point):
        if Button.check(self, point):
            self.on = not self.on
            return True
        return False

    def display(self, surface):
        if self.on:
            surface.blit(buttonon, self.pos())
        else:
            surface.blit(buttonoff, self.pos())
        surface.blit(self.text, self.textrect)


