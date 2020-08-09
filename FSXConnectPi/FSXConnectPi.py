#FSXConnectPi
import time
#gui
import mainui
gui=mainui.MainUI()
#rotary encoder
import rotaryencoder
enc=rotaryencoder.RotaryEncoder(18,17,27)
enc2=rotaryencoder.RotaryEncoder(23,22,24)
#udp
import udp

gui.running=True
lastrendertime = 0

try:
    while gui.running:
        #time.sleep(0.001)

        #enc1
        dir=enc.getdirection()
        if dir== 1:
            udp.udpsend(bytes([1]))
        elif dir==-1:
            udp.udpsend(bytes([2]))
        if enc.getbutton():
            print('press')
            
        #enc2
        dir2=enc2.getdirection()
        if dir2== 1:
            print('2 right')
        elif dir2==-1:
            print('2 left')
        if enc2.getbutton():
            print('2 press')
            
        #gui event
        if gui.getevent():
            print('event')
            
        #gui render
        rendertime = time.time()-lastrendertime
        if rendertime>0.3:
            gui.render()
            lastrendertime=time.time()
            
except KeyboardInterrupt:
    print('quit')
    
    
