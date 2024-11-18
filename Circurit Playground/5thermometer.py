from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.05

import time

while True:     
    temp_c = cp.temperature
    temp_f = (temp_c * 9/5) + 32
    if temp_f < 78:
        cp.pixels[0] = ((0, 0, 255))
    if temp_f > 78:
        cp.pixels[1] = ((28, 0, 227))
    if temp_f > 79:
        cp.pixels[2] = ((57, 0, 199))
    if temp_f > 80:
        cp.pixels[3] = ((85, 0, 170))
    if temp_f > 81:
        cp.pixels[4] = ((113, 0, 142))
    if temp_f > 82:
        cp.pixels[5] = ((142, 0, 113))
    if temp_f > 83:
        cp.pixels[6] = ((170, 0, 85))
    if temp_f > 84:
        cp.pixels[7] = ((199, 0, 57))
    if temp_f > 85:
        cp.pixels[8] = ((227, 0, 28))
    if temp_f > 86:
        cp.pixels[9] = ((255, 0, 0))
    time.sleep(0.5)