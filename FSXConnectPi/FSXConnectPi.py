#FSXConnectPi
import time
#gui
import mainui
gui=mainui.MainUI()
#rotary encoder
import rotaryencoder
enc=rotaryencoder.RotaryEncoder(17,18,27)

gui.running=True
lastrendertime = 0
while gui.running:
    #time.sleep(0.001)

    dir=enc.getdirection()
    if dir== 1:
        print('rotate right')
    elif dir==-1:
        print('left')
    if enc.getbutton():
        print('press')
        
    #gui event
    if gui.getevent():
        print('event')
        
    #gui render
    rendertime = time.time()-lastrendertime
    if rendertime>0.1:
        gui.render()
        lastrendertime=time.time()
