# Imports the tools needed to interact with the board
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.05

# Everything that you write will go inside the while true loop
while True:     

    # The list cp.pixels is how you interact with the pixels
    # A pixel is made up of three LEDs, red, green, and blue
    # LEDs are manufactured to display one color
    # LEDs change brightness based on how much power they receive
    # The three values you set pixel to are (red, green, blue)
    if cp.switch:
        cp.pixels[0] = ((0, 255, 0))
        cp.pixels[1] = ((0, 255, 0))
        cp.pixels[2] = ((0, 255, 0))
        cp.pixels[3] = ((0, 255, 0))
        cp.pixels[4] = ((0, 255, 0))
        cp.pixels[5] = ((0, 0, 0))
        cp.pixels[6] = ((0, 0, 0))
        cp.pixels[7] = ((0, 0, 0))
        cp.pixels[8] = ((0, 0, 0))
        cp.pixels[9] = ((0, 0, 0))
    else:
        cp.pixels[0] = ((0, 0, 0))
        cp.pixels[1] = ((0, 0, 0))
        cp.pixels[2] = ((0, 0, 0))
        cp.pixels[3] = ((0, 0, 0))
        cp.pixels[4] = ((0, 0, 0))
        cp.pixels[5] = ((0, 255, 0))
        cp.pixels[6] = ((0, 255, 0))
        cp.pixels[7] = ((0, 255, 0))
        cp.pixels[8] = ((0, 255, 0))
        cp.pixels[9] = ((0, 255, 0))
# If you have a single red light on your board, its working!
# ...remember to save...
