from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.05

import time
import random
x = 0
while True:     
    if cp.button_a:
        cp.pixels.fill((0, 0, 0))
        x = x + 1
        for i in range(x):
            cp.pixels[i] = (255, 0, 225)
        time.sleep(.400)
    if cp.button_b:
        cp.pixels.fill((0 ,0 ,0))
        x = x - 1
        for i in range(x):
            cp.pixels[i] = (255, 0, 225)
        time.sleep(.400)
        