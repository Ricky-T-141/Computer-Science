print("You are going to be classifing what category a hurricane is.")

speed = int(input("How many miles per hour is the wind speed?\n"))

if (speed < 74):
    print("Tropical Storm")
elif (speed < 96):
    print("Category 1")
elif (speed < 111):
    print("Category 2")
elif (speed < 130):
    print("Category 3")
elif (speed < 157):
    print("Category 4")
else:
    print("Category 5")