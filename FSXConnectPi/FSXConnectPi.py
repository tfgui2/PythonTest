#FSXConnectPi
from ClientEvents import *
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


actiontable=[
    # button,  rotate right,  rotate left
    [EVENT_NONE, EVENT_NONE, EVENT_NONE],
    [COM_STBY_RADIO_SWAP, COM_RADIO_WHOLE_INC, COM_RADIO_WHOLE_DEC],
    [COM2_RADIO_SWAP, COM2_RADIO_WHOLE_INC, COM2_RADIO_WHOLE_DEC],
    [NAV1_RADIO_SWAP, NAV1_RADIO_WHOLE_INC, NAV1_RADIO_WHOLE_DEC],
    [NAV2_RADIO_SWAP, NAV2_RADIO_WHOLE_INC, NAV2_RADIO_WHOLE_DEC],
    [GPS_CURSOR_BUTTON, GPS_GROUP_KNOB_INC, GPS_GROUP_KNOB_DEC],
    ]

actiontable2=[
    # button,  rotate right,  rotate left
    [EVENT_NONE, EVENT_NONE, EVENT_NONE],
    [COM_STBY_RADIO_SWAP, COM_RADIO_FRACT_INC, COM_RADIO_FRACT_DEC],
    [COM2_RADIO_SWAP, COM2_RADIO_FRACT_INC, COM2_RADIO_FRACT_DEC],
    [NAV1_RADIO_SWAP, NAV1_RADIO_FRACT_INC, NAV1_RADIO_FRACT_DEC],
    [NAV2_RADIO_SWAP, NAV2_RADIO_FRACT_INC, NAV2_RADIO_FRACT_DEC],
    [GPS_CURSOR_BUTTON, GPS_PAGE_KNOB_INC, GPS_PAGE_KNOB_DEC],
    ]

# encoder run
def encoder_run():
    eventid=EVENT_NONE
    #enc1
    rotate=enc.getdirection()
    if rotate!=0: # 0 is no rotate
        eventid=actiontable[gui.state][rotate]
    elif enc.getbutton():
        eventid=actiontable[gui.state][0]
                    
    #enc2
    rotate=enc2.getdirection()
    if rotate!=0:
        eventid=actiontable2[gui.state][rotate]
    elif enc2.getbutton():
        eventid=actiontable2[gui.state][0]
    
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
    
    
