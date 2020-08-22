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


activefreq=0
stbyfreq=0

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

def processreply(reply):
    if reply==None:
        return
    
    temp1=reply.decode('utf-8')
    print(temp1)
    temp=temp1.split(',')
    
    requestid=int(temp[0])
    if requestid in (100,101,102,103):
        global activefreq
        global stbyfreq
        activefreq=int(temp[1])
        stbyfreq=int(temp[2])
        drawfreq()
    elif requestid ==104:
        states=[]
        for t in temp[1:]:
            if t=='0':
                states.append(False)
            else:
                states.append(True)
        gui.setaptoggle(states)
    else:
        print('nono:', temp[0])
        
        
def drawfreq():
    global activefreq
    global stbyfreq
    print(activefreq)
    str='%d <-> %d'%(activefreq+10000,stbyfreq+10000)
    gui.drawtext(2, str)
                     

def getrequest(event_id):
    requestid=request_ids.get(event_id)
    if requestid:
        return requestid
    return 0

        
# main loop
lastrendertime = 0
while gui.running:
    #time.sleep(0.001)

    #rotary input
    event_id=encoder_run()
    if event_id>EVENT_NONE:
        udp.udpbytesend(event_id)
        req=getrequest(event_id)
        if req>0:
            udp.udpbytesend(req)
        
    #gui event
    gui.run()
    event_id=gui.getevent()
    if event_id>EVENT_NONE:
        udp.udpbytesend(event_id)
        req=getrequest(event_id)
        if req>0:
            udp.udpbytesend(req)
    else:
        request=gui.requestdata
        if request>0:
            udp.udpbytesend(request)
            
    #gui render
    if (time.time()-lastrendertime)>0.05:
        if gui.render():
            lastrendertime=time.time()
        
    #udp receive
    """
    try:
        reply=udp.udpreceive()
        processreply(reply)
    except:
        pass
    """
    reply=udp.udpreceive()
    if reply:
        processreply(reply)
    
    
