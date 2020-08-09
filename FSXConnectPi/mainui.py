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
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

btnmode=ui_button.ModeButton((35,50))
btnlabel= [
    ['a','b','c','d','e','f'],
    ['1','2','3','4','5','6','7','8','9','10'],
    ['1','2','3','4','5','6'],
    ['1','2','3','4','5','6'],
    ['1','2','3','4','5','6'],
    ['1','2','3','4','5','6'],
    ['1','2','3','4','5','6'],
    ]
modelabel=['auto','audio','com1','com2','nav1','nav2','','','','','']
#states=('ap', 'au', 'com1', 'com2', 'nav1', 'nav2')
#togglememory=[]
togglememory=[[0,0,0,0,0, 0,0,0,0,0]]*len(modelabel)


class MainUI:
    def __init__(self):
        self.state=0
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
            
        
    def buttonselectstate(self, buttonid):
        if buttonid<len(btnlabel):
            self.state=buttonid
        btnmode.on=False
        self.updatelabels()
        
        
    def getevent(self):
        if self.running==False:
            return
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close()
                return True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = event.pos
                for bt in self.buttons:
                    if bt.check(mousepos):
                        self.processbutton(bt.id)
                        return True
                if btnmode.check(mousepos):
                    if btnmode.on:
                        self.updatetogglememory()
                    self.updatelabels()
                    return True
        return False
    
    
    def displaytext(self):
        boxleft=200
        boxtop=50
        boxwidth=460
        boxheight=120
        pygame.draw.rect(screen, green, [200,50,460,120])
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
        gui.getevent()
        gui.render()
    
