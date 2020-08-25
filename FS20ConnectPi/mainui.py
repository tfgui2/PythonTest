#main ui
from setting import *
from ClientEvents import *
from ClientRequests import *
from rotaryevents import *


import time
import pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption('FS20ConnectPI')

if IS_FULLSCREEN:
    screen = pygame.display.set_mode((800,480), pygame.FULLSCREEN)
    pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
else:
    screen = pygame.display.set_mode((800,480))

font1 = pygame.font.Font('freesansbold.ttf', 16)
font2 = pygame.font.Font('freesansbold.ttf', 30)
green = (0, 210, 0)
blue = (0, 0, 128)
bgcolor=(30,30,60)


import ui_button


class MainUI:
    def __init__(self):
        self.buttons = []
        self.makebuttons()
        self.reset()
        
    def reset(self):
        self.buttondown=False
        self.mousepos=0
        self.isdirt=True
        self.eventid=EVENT_NONE
        self.requestid=0
        self.processbutton(0)
        
    def addbutton(self, pos, toggle=False):
        id=len(self.buttons)
        btn=ui_button.ToggleButton(id, pos)
        btn.settoggleenable(toggle)
        self.buttons.append(btn)
        
    def makebuttons(self):
        #buttonid : 0 ~ 9
        dx=130
        x=50
        y=110
        for i in range(3):
            self.addbutton((x,y))
            x +=dx
        x=50
        y=300
        for i in range(3):
            self.addbutton((x,y))
            x +=dx
            
        btnlabels=['nav freq', 'hdg/vor', 'Alt/vs', 'G500', 'G1000PFD', 'G1000MFD']
        i=0
        for bt in self.buttons:
            bt.setlabel(btnlabels[i])
            i+=1
        
    def enc1text(self, text):
        self.text1 = font2.render(text, True, green)
        self.isdirt=True
        
    def enc2text(self, text):
        self.text2 = font2.render(text, True, green)
        self.isdirt=True
        
    def render_enc(self):
        x=780
        line1 = 100
        line2 = 330
        screen.blit(self.text1, (x-self.text1.get_width(),line1))
        screen.blit(self.text2, (x-self.text2.get_width(),line2))
        
    def render_buttons(self):
        for bt in self.buttons:
            bt.displayforce(screen)

    def render(self):
        if self.isdirt==False:
            return False
        self.isdirt=False
        
        # rendering start
        screen.fill(bgcolor)
        
        # enctext
        self.render_enc()
        
        # buttons
        self.render_buttons()

        if self.buttondown:
            pygame.draw.circle(screen, green, self.mousepos, 60)

        pygame.display.update()
        return True
        
    def close(self):
        pygame.quit()

    def run(self):
        self.eventid=EVENT_NONE
        self.requestid=0
        
        for event in pygame.event.get():
            self.isdirt=True
            if event.type == pygame.QUIT:
                return False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mousepos = event.pos
                self.buttondown=True
                self.checkbutton(event.pos)
                
            elif event.type == pygame.MOUSEBUTTONUP:
                self.buttondown=False
                
        return True
    
    def checkbutton(self, mousepos):
        for bt in self.buttons:
            if bt.check(mousepos):
                self.processbutton(bt.id)
                return
    
    def processbutton(self, buttonid):
        if buttonid==0:
            self.enc1state=RE_NAV1_WHOLE
            self.enc2state=RE_NAV1_FRACT
            self.enc1text('Nav 1')
            self.enc2text('Nav 1')
        elif buttonid==1:
            self.enc1state=RE_HDG_BUG
            self.enc2state=RE_VOR_BUG
            self.enc1text('HDG')
            self.enc2text('VOR 1')
        elif buttonid==2:
            self.enc1state=RE_ALT_VAR
            self.enc2state=RE_VS_VAR
            self.enc1text('Alt')
            self.enc2text('Vs')
        elif buttonid==3:
            self.enc1state=RE_G500_GROUP
            self.enc2state=RE_G500_PAGE
            self.enc1text('G500')
            self.enc2text('G500')
        elif buttonid==4:
            self.enc1state=RE_G1000_PFD_GROUP
            self.enc2state=RE_G1000_PFD_PAGE
            self.enc1text('G1000PFD')
            self.enc2text('G1000PFD 1')
        elif buttonid==5:
            self.enc1state=RE_G1000_MFD_GROUP
            self.enc2state=RE_G1000_MFD_PAGE
            self.enc1text('G1000MFD')
            self.enc2text('G1000MFD')
        
            
    
    def getevent(self):
        return self.eventid
    
    def getrequest(self):
        return self.requestid
                
    def getenc1state(self):
        return self.enc1state
    
    def getenc2state(self):
        return self.enc2state
        
if __name__=='__main__':
    gui=MainUI()
    
    while True:
        time.sleep(0.001)
        if gui.run()==False:
            break
        gui.render()
    
    gui.close()

