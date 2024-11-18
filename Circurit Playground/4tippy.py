from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.05

import time

while True:     
    x, y, z = cp.acceleration
    if x < -5:
        cp.pixels[0] = ((0, 0, 0))
        cp.pixels[1] = ((0, 0, 0))
        cp.pixels[2] = ((0, 0, 0))
        cp.pixels[3] = ((0, 0, 0))
        cp.pixels[4] = ((0, 0, 0))
        cp.pixels[5] = ((0, 0, 0))
        cp.pixels[6] = ((255, 0, 0))
        cp.pixels[7] = ((255, 0, 0))
        cp.pixels[8] = ((255, 0, 0))
        cp.pixels[9] = ((0, 0, 0))
    elif x > 5:
        cp.pixels[0] = ((0, 0, 0))
        cp.pixels[1] = ((0, 255, 0))
        cp.pixels[2] = ((0, 255, 0))
        cp.pixels[3] = ((0, 255, 0))
        cp.pixels[4] = ((0, 0, 0))
        cp.pixels[5] = ((0, 0, 0))
        cp.pixels[6] = ((0, 0, 0))
        cp.pixels[7] = ((0, 0, 0))
        cp.pixels[8] = ((0, 0, 0))
        cp.pixels[9] = ((0, 0, 0))