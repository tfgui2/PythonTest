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
import ui_page

class MainUI:
    def __init__(self):
        self.makepage()
        self.reset()
        
    def reset(self):
        self.buttondown=False
        self.mousepos=0
        self.isdirt=True
        self.eventid=EVENT_NONE
        self.requestid=0
        self.pageid=0
        self.processbutton(0)
        self.selectpage(self.pageid)
        self.setfreq('activefreq','stbyfreq')
        
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
        
    def makepage(self):
        self.pagebuttons=[]
        
        btn=ui_button.RectButton(0, pygame.Rect(0,0, 100, 240))
        btn.setlabel('page1')
        self.pagebuttons.append(btn)
        
        btn=ui_button.RectButton(1, pygame.Rect(0,240, 100, 240))
        btn.setlabel('page2')
        self.pagebuttons.append(btn)
        
        self.pages=[]
        
        page=ui_page.Page(pygame.Rect(100,0, 500, 480))
        self.pages.append(page)
        
        btnlabels=['nav freq', 'hdg/vor', 'Alt/vs', 'G500', 'G1000PFD', 'G1000MFD']
        for i in range(3):
            b=ui_button.ToggleButton(i, (0,0))
            x=i*130 + 100
            y=100
            page.addbutton(b, (x,y), btnlabels[b.id])
   
        for i in range(3):
            b=ui_button.ToggleButton(i+3, (0,0))
            x=i*130 + 100
            y=300
            page.addbutton(b, (x,y), btnlabels[b.id])
            
        page=ui_page.Page(pygame.Rect(100,0, 500, 480))
        self.pages.append(page)
            
    def render_page(self):
        for bt in self.pagebuttons:
            bt.displayforce(screen)
        page=self.pages[self.pageid]
        page.display(screen)

    def render(self):
        if self.isdirt==False:
            return False
        self.isdirt=False
        
        # rendering start
        screen.fill(bgcolor)
        
        # page menu
        self.render_page()
        
        # enctext
        self.render_enc()
        
        self.render_freq()
        
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
                self.checkpage(event.pos)
                
            elif event.type == pygame.MOUSEBUTTONUP:
                self.buttondown=False
                
        return True
    
    def checkpage(self, mousepos):
        for pg in self.pagebuttons:
            if pg.check(mousepos):
                self.selectpage(pg.id)
                return
        page=self.pages[self.pageid]
        btid=page.checkbutton(mousepos)
        if btid>=0:
            self.processbutton(btid)
            
    def selectpage(self, pageid):
        self.pageid=pageid
        for pg in self.pagebuttons:
            if pg.id==pageid:
                pg.setonoff(True)
            else:
                pg.setonoff(False)
  
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
    
    def processreply(self, reply):
        requestid=int(reply[0])
        if requestid in (100,101,102,103):
            af=10000+int(reply[1])
            sf=10000+int(reply[2])
            self.setfreq('%d'%af,'%d'%sf)
            
    def setfreq(self, actf, stbf):
        self.activefreq = font2.render(actf, True, green)
        self.stbyfreq = font2.render(stbf, True, green)
        self.isdirt=True
        
    def render_freq(self):
        x=600
        line1 = 200
        line2 = 240
        screen.blit(self.activefreq, (x,line1))
        screen.blit(self.stbyfreq, (x,line2))
    
        
    
        
if __name__=='__main__':
    gui=MainUI()
    
    while True:
        time.sleep(0.001)
        if gui.run()==False:
            break
        gui.render()
    
    gui.close()

