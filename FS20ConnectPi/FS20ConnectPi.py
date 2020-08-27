# FS20connectPi
from ClientEvents import *
from ClientRequests import *


#udp
import udp


#gui
import mainui
gui=mainui.MainUI()


#rotary encoder
import rotaryencoder
from rotaryevents import *

enc1=rotaryencoder.RotaryEncoder(18,17,27)
enc2=rotaryencoder.RotaryEncoder(23,22,24)

def encoder_run(enc, rotarystate):
    eventid=EVENT_NONE
    events=RE_EVENTS.get(rotarystate)
    if events == None:
        return
    rotate=enc.getdirection()
    if rotate!=0: # 0 is no rotate
        eventid=events[rotate]   
    elif enc.getbutton():
        eventid=events[0]
    return eventid


# receive process
def processreply(reply):
    if reply==None:
        return
    
    temp1=reply.decode('utf-8')
    temp=temp1.split(',')
    gui.processreply(temp)



# main loop
import time
lastrendertime = 0
while True:
    time.sleep(0.001)

    #rotary input
    event_id=encoder_run(enc1, gui.getenc1state())
    if event_id>EVENT_NONE:
        udp.udpbytesend(event_id)
        #request
        if gui.getenc1state()==RE_NAV1_WHOLE:
            udp.udpbytesend(REQ_NAV1_FREQ)
        
    event_id=encoder_run(enc2, gui.getenc2state())
    if event_id>EVENT_NONE:
        udp.udpbytesend(event_id)
        #request
        if gui.getenc2state()==RE_NAV1_FRACT:
            udp.udpbytesend(REQ_NAV1_FREQ)
        
    #gui event
    if gui.run() == False:
        break
    
    event_id=gui.getevent()
    if event_id>EVENT_NONE:
        udp.udpbytesend(event_id)
        
    request_id=gui.getrequest()
    if request_id>0:
        udp.udpbytesend(request_id)
            
    #gui render
    if (time.time()-lastrendertime)>0.05:
        if gui.render():
            lastrendertime=time.time()
        
    # udp receive
    reply=udp.udpreceive()
    if reply:
        processreply(reply)
        
gui.close()
