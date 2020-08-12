#main ui
from setting import *
from ClientEvents import *
from UITable import *

import pygame
import ui_button
pygame.init()
pygame.font.init()
pygame.display.set_caption('FSXConnectPI')

if IS_FULLSCREEN:
    screen = pygame.display.set_mode((720,480), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((720,480))

font1 = pygame.font.Font('freesansbold.ttf', 16)
font2 = pygame.font.Font('freesansbold.ttf', 30)
green = (0, 210, 0)
blue = (0, 0, 128)
if IS_FULLSCREEN:
    pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

btnmode=ui_button.ModeButton((35,40))
#init togglememory
togglememory=[[0,0,0,0,0, 0,0,0,0,0]]*STATE_END
def inittogglememory():
    global togglememory
    togglememory=[[0,0,0,0,0, 0,0,0,0,0]]*STATE_END
    print('init toggle')


class MainUI:
    def __init__(self):
        self.state=STATE_COM1
        self.substate=0
        self.eventid=0
        self.requestdata=0
        self.running=True
        self.buttondown=False
        self.mousepos=0
        self.isdirt=True
    
        ### resource
        self.background = pygame.image.load('background.bmp')
        ### buttons
        self.buttons = []
        self.makebuttons()
        # rendering start
        screen.blit(self.background, (0,0))
        text = font1.render('FSXConnectPI', True, green, blue)
        screen.blit(text, (20,15))
        self.displaytext()
        
    def reset(self):
        self.state=STATE_COM1
        self.substate=0
        self.eventid=0
        self.requestdata=0
        self.running=True
        self.buttondown=False
        self.mousepos=0
        self.isdirt=True
        btnmode.setonoff(False)
        self.displaytext()
        self.updatelabels()
        inittogglememory()
          
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
            self.addbutton(i, (x,y))
            x +=dx
        self.updatelabels()
        
        
    def updatetogglememory(self):
        toggles=[]
        for b in self.buttons:
            toggles.append(b.on)
        togglememory[self.state]=toggles
        print('update toggle')
        
    def restoretoggle(self):
        toggles=togglememory[self.state]
        i=0
        for b in self.buttons:
            b.on=toggles[i]
            i+=1
        print('restor toggle')
        
            
    def updatelabels(self):
        if btnmode.on:
            self.updatestatelabels()
            return
        labels=buttonlabels.get(self.state)
        if labels:
            index=0
            for b in self.buttons:
                if index<len(labels):
                    b.setlabel(labels[index])
                else:
                    b.setlabel('')
                index+=1
        self.restoretoggle()
            
    def updatestatelabels(self):
        index=0
        for b in self.buttons:
            label=statelabel[index]
            b.setlabel(label)
            if index==self.state:
                b.on=True
            else:
                b.on=False
            index+=1
            
    def setaptoggle(self, states):
        index=0
        for s in states:
            self.buttons[index].setonoff(s)
            index +=1
        self.isdirt=True
 

    ######################################################
    #
    def processbutton(self, buttonid):
        if btnmode.on:
            self.selectstate(buttonid)
            return
        actions=buttonactions.get(self.state)
        if actions:
            if buttonid<len(actions):
                self.eventid=actions[buttonid]
                if self.eventid in request_ids.keys():
                    self.requestdata=request_ids.get(self.eventid)
        else:
            self.selectsubstate(buttonid)
    
    def selectstate(self, buttonid):
        if buttonid==9: #quit
            self.close()
            return
        elif buttonid==8: #reset
            self.reset()
            return
        
        if buttonid<STATE_END:
            self.state=buttonid
            self.substate=0
            # gps로 변경시 panel_3
            if self.state==STATE_GPS:
                self.eventid=PANEL_3
            elif self.state==STATE_COM1:
                self.requestdata=request_ids.get(COM_RADIO_WHOLE_DEC)
            elif self.state==STATE_AUTO:
                self.requestdata=request_ids.get(AP_MASTER)
            
                
            
        btnmode.setonoff(False)
        self.displaytext()
        self.updatelabels()
        
    def selectsubstate(self, buttonid):
        if buttonid<len(buttonlabels.get(self.state)):
            self.substate=self.state*10+buttonid
            for b in self.buttons:
                if b.id==buttonid:
                    b.setonoff(True)
                else:
                    b.setonoff(False)
        

    def run(self):
        self.eventid=0
        self.requestdata=0
        
        if self.running==False:
            return
        
        for event in pygame.event.get():
            self.isdirt=True
            if event.type == pygame.QUIT:
                self.close()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = event.pos
                self.buttondown=True
                print(self.buttondown)
                self.mousepos=mousepos
                for bt in self.buttons:
                    if bt.check(mousepos):
                        self.processbutton(bt.id)
                        
                if btnmode.check(mousepos):
                    if btnmode.on:
                        self.updatetogglememory()
                    self.updatelabels()
            elif event.type == pygame.MOUSEBUTTONUP:
                self.buttondown=False
                print(self.buttondown)
                
    
    def getevent(self):
        return self.eventid
    
    def getrotarystate(self):
        if self.substate>0:
            return self.substate
        return self.state
    
    def drawtext(self,line,str):
        self.isdirt=True
        if line==2:
            self.text2=font2.render(str, True, blue)
        
    def displaytext(self):
        self.isdirt=True
        self.text = font2.render(statelabel[self.state], True, blue)
        self.text2= font2.render('hello world', True, blue)
        
        
    def renderdisplay(self):
        pygame.draw.rect(screen, green, [210,45,450,90])
        x=230
        line1 = 60
        line2 = 100
        screen.blit(self.text, (x,line1))
        screen.blit(self.text2, (x,line2)) 
          
    def render(self):
        if self.running==False:
            return False
        
        if self.isdirt==False:
            return False
        self.isdirt=False
        
        # rendering start
        screen.blit(self.background, (0,0))
        
        # display text
        self.renderdisplay()
        
        # display buttons
        #btnmode.display(screen)
        btnmode.displayforce(screen)
        for bt in self.buttons:
            #bt.display(screen)
            bt.displayforce(screen)
            
        if self.buttondown:
            pygame.draw.circle(screen, green, self.mousepos, 60)

        pygame.display.update()
        return True
        
        
    def close(self):
        self.running = False
        pygame.quit()
        
        
if __name__=='__main__':
    gui=MainUI()
    
    while gui.running:
        gui.run()
        gui.getevent()
        gui.render()
    
