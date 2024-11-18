from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.05

import time

while True:     
    if cp.button_a:
        for i in range(0,10):
            cp.pixels[i] = (0, 0, 255)
            time.sleep(.1)
            cp.pixels[i] = (0, 0, 0)