#FSXConnectPi
from ClientEvents import *
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

def encoder_run():
    eventid=EVENT_NONE
    #enc1
    dir1=enc.getdirection()
    if dir1== 1:
        eventid=COM_RADIO_WHOLE_INC
    elif dir1==-1:
        eventid=COM_RADIO_WHOLE_DEC
    if enc.getbutton():
        eventid=COM_STBY_RADIO_SWAP
    #enc2
    dir2=enc2.getdirection()
    if dir2== 1:
        eventid=COM_RADIO_FRACT_INC
    elif dir2==-1:
        eventid=COM_RADIO_FRACT_DEC
    if enc2.getbutton():
        eventid=COM_STBY_RADIO_SWAP
    
    return eventid
    

try:
    while gui.running:
        #time.sleep(0.001)

        #input
        event_id=encoder_run()
        if event_id>EVENT_NONE:
            udp.udpbytesend(event_id)
        #gui event
        gui.run()
        event_id=gui.getevent()
        if event_id>EVENT_NONE:
            udp.udpbytesend(event_id)
            
            
        #gui render
        rendertime = time.time()-lastrendertime
        if rendertime>0.3:
            gui.render()
            lastrendertime=time.time()
            
except KeyboardInterrupt:
    print('quit')
    
    
