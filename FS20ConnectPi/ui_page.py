import ui_button
import pygame
# page

class Page:
    def __init__(self, rect):
        self.rect=rect
        self.buttons=[]
        pass
    
    def addbutton(self, b, pos, label):
        b.rect.left=self.rect.left+pos[0]
        b.rect.top=self.rect.top+pos[1]
        b.setlabel(label)
        self.buttons.append(b)
    
    def display(self, surface):
        for bt in self.buttons:
            bt.displayforce(surface)
            
    def checkbutton(self, mousepos):
        for bt in self.buttons:
            if bt.check(mousepos):
                return bt.id
        return -1
        
    
    