import time
import rotaryencoder
re = rotaryencoder.RotaryEncoder(17,18,27)

running=True
while running:
    time.sleep(0.001)
    
    dir=re.getdirection()
    if dir== 1:
        print('rotate right')
    elif dir==-1:
        print('left')
    if re.getbutton():
        print('press')
