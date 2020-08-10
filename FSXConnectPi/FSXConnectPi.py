#FSXConnectPi
from ClientEvents import *
from UITable import *
import time
#gui
import mainui
gui=mainui.MainUI()
gui.running=True
#rotary encoder
import rotaryencoder
enc=rotaryencoder.RotaryEncoder(18,17,27)
enc2=rotaryencoder.RotaryEncoder(23,22,24)
#udp
import udp



# encoder run
def encoder_run():
    eventid=EVENT_NONE
    #enc1
    rotate=enc.getdirection()
    if rotate!=0: # 0 is no rotate
        rotarystate=gui.getrotarystate()
        events=rotarytable.get(rotarystate)
        if events:
            eventid=events[rotate]
    elif enc.getbutton():
        rotarystate=gui.getrotarystate()
        events=rotarytable.get(rotarystate)
        if events:
            eventid=events[0]
                    
    #enc2
    rotate=enc2.getdirection()
    if rotate!=0:
        rotarystate=gui.getrotarystate()
        events=rotarytable2.get(rotarystate)
        if events:
            eventid=events[rotate]
    elif enc2.getbutton():
        rotarystate=gui.getrotarystate()
        events=rotarytable2.get(rotarystate)
        if events:
            eventid=events[0]
    
    return eventid
    

# main loop
try:
    lastrendertime = 0
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
        if (time.time()-lastrendertime)>0.3:
            gui.render()
            lastrendertime=time.time()
            
except KeyboardInterrupt:
    print('quit')
    
    

