import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

clk = 17
dt = 18

list = [clk, dt]

for i in list:
  GPIO.setup(i, GPIO.IN, GPIO.PUD_DOWN)

clkLastState = GPIO.input(clk)
counter = 0
running = True

try:
  while running:
    clkState = GPIO.input(clk)
    dtState = GPIO.input(dt)
    time.sleep(0.001)
    print("clk:", clkState, " dt:", dtState)

except KeyboardInterrupt:
  GPIO.cleanup()
  running = False

