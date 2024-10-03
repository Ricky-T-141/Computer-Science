print("You are going to pick three random words")
word_1 = input("Pick your first word\n-")
word_2 = input("Pick your second word\n-")
word_3 = input("Pick your third word\n-")
print("Your words in order are " + word_1 + ", " + word_2 + ", and " + word_3 + "!")



def add_three(x, y, z):
    print(x + y + z)
number_1 = int(input("Choose an integer\n-"))
number_2 = int(input("Choose a second integer\n-"))
number_3 = int(input("Choose a third integer\n-"))

add_three(number_1, number_2, number_3)



def data_three():
    word = input("Choose a word\n-")
    integer = int(input("Now choose an integer\n-"))
    integer = str(integer)
    float_1 = float(input("Finally choose a float\n-"))
    float_1 = str(float_1) 
    print("The sum of " + integer + " and " + float_1 + " is " + str(integer + float_1) + ", and that is number, in millions, that the word " + word + " has been used in the world.")

data_three()            #No idea how to add integer and float