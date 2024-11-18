# Guess the number
import random
your_num = ""
rand_num = int(random.randint(1,101))

while your_num != rand_num:
    your_num = int(input("Pick a number 1 through 100\n"))
    if your_num < rand_num:
        print("Incorrect: Higher")
        print("Try again")
    elif your_num > rand_num:
        print("Incorrect: Lower")
        print("Try again")
    else:
        print("CORRECT!!!")
print("Good stuff!")