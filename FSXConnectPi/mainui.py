#main ui
from ClientEvents import *
import pygame
import ui_button
pygame.init()
pygame.font.init()
pygame.display.set_caption('FSXConnectPI')
IS_FULLSCREEN=False
if IS_FULLSCREEN:
    screen = pygame.display.set_mode((720,480), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((720,480))

font1 = pygame.font.Font('freesansbold.ttf', 16)
font2 = pygame.font.Font('freesansbold.ttf', 30)
green = (0, 210, 0) 
blue = (0, 0, 128)
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

btnmode=ui_button.ModeButton((35,50))

STATE_AUTO=0
STATE_AUDIO=1
STATE_COM1=2
STATE_COM2=3
STATE_NAV1=4
STATE_NAV2=5
modelabel=['auto','audio','com1','com2','nav1','nav2','','','','','']
btnlabel= [
    ['a','b','c','d','e','f'],
    ['1','2','3','4','5','6','7','8','9','10'],
    ['1','2','3','4','5','6'],
    ['1','2','3','4','5','6'],
    ['1','2','3','4','5','6'],
    ['1','2','3','4','5','6'],
    ['1','2','3','4','5','6'],
    ]

togglememory=[[0,0,0,0,0, 0,0,0,0,0]]*len(modelabel)


class MainUI:
    def __init__(self):
        self.state=STATE_AUDIO
        self.eventid=0
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
          
    def addbutton(self, id, pos, toggle=False):
        btn=ui_button.ToggleButton(id, pos)
        btn.settoggleenable(toggle)
        self.buttons.append(btn)     
        
    def makebuttons(self):
        #buttonid : 0 ~ 9
        dx=130
        x=50
        y=210
        for i in range(5):
            self.addbutton(i, (x,y))
            x +=dx
        x=50
        y=340
        for i in range(5,10):
            self.addbutton(i, (x,y), True)
            x +=dx
            
        self.updatelabels()    
        
    def updatetogglememory(self):
        toggles=[]
        for b in self.buttons:
            toggles.append(b.on)
        togglememory[self.state]=toggles
    def restoretoggle(self):
        toggles=togglememory[self.state]
        i=0
        for b in self.buttons:
            b.on=toggles[i]
            i+=1
        
            
    def updatelabels(self):
        if btnmode.on:
            return self.updatemodelabels()
        
        if self.state<len(btnlabel):
            index=0
            for b in self.buttons:
                labels=btnlabel[self.state]
                if index<len(labels):
                    b.setlabel(labels[index])
                else:
                    b.setlabel('')
                index+=1
                
        self.restoretoggle()
            
    def updatemodelabels(self):
        index=0
        for b in self.buttons:
            label=modelabel[index]
            b.setlabel(label)
            if index==self.state:
                b.on=True
            else:
                b.on=False
            index+=1
 
    def processbutton(self, buttonid):
        if btnmode.on:
            self.buttonselectstate(buttonid)
            return
        
        if buttonid==9:
            self.close()
            
        if self.state==STATE_AUDIO:
            if buttonid==0:
                self.eventid=COM1_TRANSMIT_SELECT
            if buttonid==1:
                self.eventid=COM2_TRANSMIT_SELECT
            print(self.eventid)
            
            
        
    def buttonselectstate(self, buttonid):
        if buttonid<len(btnlabel):
            self.state=buttonid
        btnmode.off()
        self.updatelabels()
        
        
    def run(self):
        self.eventid=0
        if self.running==False:
            return
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = event.pos
                for bt in self.buttons:
                    if bt.check(mousepos):
                        self.processbutton(bt.id)
                        
                if btnmode.check(mousepos):
                    if btnmode.on:
                        self.updatetogglememory()
                    self.updatelabels()
                
    
    def getevent(self):
        return self.eventid
    
    
    def displaytext(self):
        boxleft=200
        boxtop=50
        boxwidth=460
        boxheight=120
        pygame.draw.rect(screen, green, [210,45,450,90])
        x=230
        line1 = 60
        line2 = 100
        text = font2.render(modelabel[self.state], True, blue)
        screen.blit(text, (x,line1))
        screen.blit(font2.render('hello world', True, blue), (x,line2)) 
        
    def render(self):
        if self.running==False:
            return
        
        # rendering start
        #screen.blit(self.background, (0,0))
        
        # display text
        self.displaytext()
        
        # display buttons
        btnmode.display(screen)
        for bt in self.buttons:
            bt.display(screen)

        pygame.display.update()
        
    def close(self):
        self.running = False
        pygame.quit()
        
        
if __name__=='__main__':
    gui=MainUI()
    
    while gui.running:
        gui.run()
        gui.getevent()
        gui.render()
    
