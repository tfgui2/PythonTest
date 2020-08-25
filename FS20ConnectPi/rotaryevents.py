from ClientEvents import *
from ClientRequests import *

# rotary encoder state
RE_NAV1_WHOLE=0
RE_NAV1_FRACT=1
RE_ALT_VAR=2
RE_VS_VAR=3
RE_HDG_BUG=4
RE_VOR_BUG=5
RE_G500_GROUP=6
RE_G500_PAGE=7
RE_G1000_PFD_GROUP=8
RE_G1000_PFD_PAGE=9
RE_G1000_MFD_GROUP=10
RE_G1000_MFD_PAGE=11

# rotary event by state : sw, right, left
RE_EVENTS={
    RE_NAV1_WHOLE:[NAV1_RADIO_SWAP, NAV1_RADIO_WHOLE_INC, NAV1_RADIO_WHOLE_DEC],
    RE_NAV1_FRACT:[NAV1_RADIO_SWAP, NAV1_RADIO_FRACT_INC, NAV1_RADIO_FRACT_DEC],
    RE_ALT_VAR:[EVENT_NONE, AP_ALT_VAR_INC, AP_ALT_VAR_DEC],
    RE_VS_VAR:[EVENT_NONE, AP_VS_VAR_INC, AP_VS_VAR_DEC],
    RE_HDG_BUG:[REQ_HDGBUG_SYNC, HEADING_BUG_INC, HEADING_BUG_DEC],
    RE_VOR_BUG:[EVENT_NONE, VOR1_OBI_DEC, VOR1_OBI_INC],
    RE_G500_GROUP:[GPS_CURSOR_BUTTON, GPS_GROUP_KNOB_INC, GPS_GROUP_KNOB_DEC],
    RE_G500_PAGE:[GPS_CURSOR_BUTTON, GPS_PAGE_KNOB_INC, GPS_PAGE_KNOB_DEC],
    RE_G1000_PFD_GROUP:[G1000_PFD_CURSOR_BUTTON, G1000_PFD_GROUP_KNOB_INC,G1000_PFD_GROUP_KNOB_DEC],
    RE_G1000_PFD_PAGE:[G1000_PFD_CURSOR_BUTTON, G1000_PFD_PAGE_KNOB_INC,G1000_PFD_PAGE_KNOB_DEC],
    RE_G1000_MFD_GROUP:[G1000_MFD_CURSOR_BUTTON, G1000_MFD_GROUP_KNOB_INC,G1000_MFD_GROUP_KNOB_DEC],
    RE_G1000_MFD_PAGE:[G1000_MFD_CURSOR_BUTTON, G1000_MFD_PAGE_KNOB_INC,G1000_MFD_PAGE_KNOB_DEC],
    }
