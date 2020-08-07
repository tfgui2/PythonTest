#button
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class Button:
    def __init__(self, pin):
        self.pin=pin
        GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
        self.state=0x1
        self.lastdebounce=0
        
    def run(self):
        elapsedtime=time.time()-self.lastdebounce
        if elapsedtime<10:
            return False
        self.lastdebounce=time.time()
        state=GPIO.input(self.pin)
        pushed=False
        if self.state>state:
            pushed=True
        self.state=state
        return pushed
    
if __name__=='__main__':
    btn=Button(27)
    while True:
        if btn.run()==True:
            print('pressed')
            