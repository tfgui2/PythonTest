import rotaryencoder
re = rotaryencoder.RotaryEncoder(2,3,4)

running=True
while running:
    if re.getdirection() != 0:
        print('rotate')
        running=False
