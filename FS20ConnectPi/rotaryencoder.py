#rotary encoder
import button
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class RotaryEncoder:
    DIR_NONE=0x0
    DIR_CW=0x10
    DIR_CCW=0x20

    R_START=0x0
    R_CW_FINAL=0x1
    R_CW_BEGIN=0x2
    R_CW_NEXT=0x3
    R_CCW_BEGIN=0x4
    R_CCW_FINAL=0x5
    R_CCW_NEXT=0x6
    
    ttable=[
        [R_START,R_CW_BEGIN,R_CCW_BEGIN,R_START],
        
        [R_CW_NEXT,R_START,R_CW_FINAL,R_START|DIR_CW],
        [R_CW_NEXT,R_CW_BEGIN,R_START,R_START],
        [R_CW_NEXT,R_CW_BEGIN,R_CW_FINAL,R_START],
        
        [R_CCW_NEXT,R_START,R_CCW_BEGIN,R_START],
        [R_CCW_NEXT,R_CCW_FINAL,R_START,R_START|DIR_CCW],
        [R_CCW_NEXT,R_CCW_FINAL,R_CCW_BEGIN,R_START],
        ]
    
    def __init__(self, pin_clk, pin_dt, pin_sw):
        self.pin1=pin_dt
        self.pin2=pin_clk
        self.sw=pin_sw
        GPIO.setup(pin_clk, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(pin_dt, GPIO.IN, GPIO.PUD_UP)
        self.state=RotaryEncoder.R_START
        self.btn=button.Button(pin_sw)
        
    def getdirection(self):
        pin1=GPIO.input(self.pin1)
        pin2=GPIO.input(self.pin2)
        pinstate=(pin2<<1)|(pin1)
        self.state=RotaryEncoder.ttable[self.state&0xf][pinstate]
        dir=self.state&0x30
        if dir==RotaryEncoder.DIR_CW:
            return 1
        elif dir==RotaryEncoder.DIR_CCW:
            return -1
        return 0
    
    def getbutton(self):
        return self.btn.run()


if __name__ == '__main__':
    enc=RotaryEncoder(2,3,4)
    dir=enc.getdirection()
    print(dir)
