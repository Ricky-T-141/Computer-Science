# Imports the tools needed to interact with the board
from adafruit_circuitplayground import cp
import time
cp.pixels.brightness = 0.05

# Everything that you write will go inside the while true loop
while True:     

    # The list cp.pixels is how you interact with the pixels
    # A pixel is made up of three LEDs, red, green, and blue
    # LEDs are manufactured to display one color
    # LEDs change brightness based on how much power they receive
    # The three values you set pixel to are (red, green, blue)
   
    cp.pixels.fill((0, 255, 0))
    time.sleep(.367)
    cp.pixels.fill((0, 0, 0))
    time.sleep(.367)
# If you have a single red light on your board, its working!
# ...remember to save...
