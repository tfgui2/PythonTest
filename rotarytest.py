import rotaryencoder
re = rotaryencoder.RotaryEncoder(17,18,4)

running=True
while running:
    dir=re.getdirection()
    if dir== 1:
        print('rotate right')
    elif dir==-1:
        print('left')
