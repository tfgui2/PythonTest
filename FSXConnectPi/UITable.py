from ClientEvents import *

STATE_AUTO=0
STATE_COM1=1
STATE_COM2=2
STATE_NAV1=3
STATE_NAV2=4
STATE_GPS=5
STATE_INST=6
STATE_END=7
SUBSTATE_HDG=60
SUBSTATE_OBS=61
SUBSTATE_END=62
# STATE  0~ max 9
# button 0~ max 9
statelabel=['AutoP','COM1','COM2','NAV1','NAV2','GPS','Instr','','reset','quit']

buttonlabels={
    STATE_AUTO:['ap','hdg','nav','apr','rev','alt','','','','nav/gps'],
    STATE_COM1:['audio','stby','stby',],
    STATE_COM2:['audio','stby','stby',],
    STATE_NAV1:['audio','stby','stby',],
    STATE_NAV2:['audio','stby','stby',],
    STATE_GPS:['nrst','msg', '', '', '', 'dir','menu','clr','ent','clrall'],
    STATE_INST:['hdg','obs']
    }

buttonactions={
    STATE_AUTO:[AP_MASTER, AP_HDG_HOLD, AP_NAV1_HOLD, AP_APR_HOLD, AP_BC_HOLD, AP_ALT_HOLD, EVENT_NONE, EVENT_NONE, EVENT_NONE, TOGGLE_GPS_DRIVES_NAV1,],
    STATE_COM1:[COM1_TRANSMIT_SELECT, COM_STBY_RADIO_SWAP, COM_STBY_RADIO_SWAP,],
    STATE_COM2:[COM2_TRANSMIT_SELECT, COM2_RADIO_SWAP, COM2_RADIO_SWAP,],
    STATE_NAV1:[RADIO_VOR1_IDENT_TOGGLE, NAV1_RADIO_SWAP, NAV1_RADIO_SWAP,],
    STATE_NAV2:[RADIO_VOR2_IDENT_TOGGLE, NAV2_RADIO_SWAP, NAV2_RADIO_SWAP,],
    STATE_GPS :[GPS_NEAREST_BUTTON, GPS_MSG_BUTTON, EVENT_NONE, EVENT_NONE, EVENT_NONE, GPS_DIRECTTO_BUTTON, GPS_MENU_BUTTON, GPS_CLEAR_BUTTON, GPS_ENTER_BUTTON, GPS_CLEAR_ALL_BUTTON],
    }
                

rotarytable={
    # button,  rotate right,  rotate left
    STATE_AUTO:[EVENT_NONE, AP_ALT_VAR_INC, AP_ALT_VAR_DEC],
    STATE_COM1:[COM_STBY_RADIO_SWAP, COM_RADIO_WHOLE_INC, COM_RADIO_WHOLE_DEC],
    STATE_COM2:[COM2_RADIO_SWAP, COM2_RADIO_WHOLE_INC, COM2_RADIO_WHOLE_DEC],
    STATE_NAV1:[NAV1_RADIO_SWAP, NAV1_RADIO_WHOLE_INC, NAV1_RADIO_WHOLE_DEC],
    STATE_NAV2:[NAV2_RADIO_SWAP, NAV2_RADIO_WHOLE_INC, NAV2_RADIO_WHOLE_DEC],
    STATE_GPS:[GPS_CURSOR_BUTTON, GPS_GROUP_KNOB_INC, GPS_GROUP_KNOB_DEC],
    SUBSTATE_HDG:[EVENT_NONE, HEADING_BUG_INC, HEADING_BUG_DEC],
    SUBSTATE_OBS:[EVENT_NONE, VOR1_OBI_DEC, VOR1_OBI_INC],
    }

rotarytable2={
    # button,  rotate right,  rotate left
    STATE_AUTO:[EVENT_NONE, AP_VS_VAR_INC, AP_VS_VAR_DEC],
    STATE_COM1:[COM_STBY_RADIO_SWAP, COM_RADIO_FRACT_INC, COM_RADIO_FRACT_DEC],
    STATE_COM2:[COM2_RADIO_SWAP, COM2_RADIO_FRACT_INC, COM2_RADIO_FRACT_DEC],
    STATE_NAV1:[NAV1_RADIO_SWAP, NAV1_RADIO_FRACT_INC, NAV1_RADIO_FRACT_DEC],
    STATE_NAV2:[NAV2_RADIO_SWAP, NAV2_RADIO_FRACT_INC, NAV2_RADIO_FRACT_DEC],
    STATE_GPS:[GPS_CURSOR_BUTTON, GPS_PAGE_KNOB_INC, GPS_PAGE_KNOB_DEC],
    SUBSTATE_HDG:[EVENT_NONE, HEADING_BUG_INC, HEADING_BUG_DEC],
    SUBSTATE_OBS:[EVENT_NONE, VOR2_OBI_DEC, VOR2_OBI_INC],
    }    
                
#request ids
request_ids={
    COM_RADIO_WHOLE_DEC:100,
    COM_RADIO_WHOLE_INC:100,
    COM_RADIO_FRACT_DEC:100,
    COM_RADIO_FRACT_INC:100,
    
    COM2_RADIO_WHOLE_DEC:101,
    COM2_RADIO_WHOLE_INC:101,
    COM2_RADIO_FRACT_DEC:101,
    COM2_RADIO_FRACT_INC:101,
    
    NAV1_RADIO_WHOLE_DEC:102,
    NAV1_RADIO_WHOLE_INC:102,
    NAV1_RADIO_FRACT_DEC:102,
    NAV1_RADIO_FRACT_INC:102,
    
    NAV2_RADIO_WHOLE_DEC:103,
    NAV2_RADIO_WHOLE_INC:103,
    NAV2_RADIO_FRACT_DEC:103,
    NAV2_RADIO_FRACT_INC:103,

    AP_BUTTONS:104,
    }
