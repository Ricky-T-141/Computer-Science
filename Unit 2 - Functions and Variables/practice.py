print("Hello, world!")          # "Hello, world!" is the peramiter
input("Please enter your username\n-")  # \n is called an escape character
# \n starts a new line (Linebreak)
# input is never required

#variables
#syntax
#<name> = <value>
x = 5

#snaking nameing convention - all lowercase, underscore for spaces
# concise: short and descriptive
username = "osowski"        #define string
fav_animal = "duck"         #define string
total_number = 12           #define integers (whole numbers)
percent_complete = 3.14     #define float (decimal number)
is_cool = True              #define boolean (true/false)
first_letter = 'c'          #define character (single symbol)

total_number = 8            # reassign



# Arathmetic operations
# + - * / ** % //
print(4 + 4)        #>8
print("4 + 4")      #>44
print("cat" + "dog")    #>catdog
print("cat" * 3)        #>catcatcat
print("cat" + 3)        #>error: cannot use + for string and int

#make some working programs
#1. add tow numbers using input
x = int(input("what is x?\n-"))     #input() always returns a string
y = input("what is y?\n-")          # even if you type in a number
y = int(y)                          #convert for string to int
print(x + y)

#2. Convertes celcius to ferenhight
temp_celcius = input("What is the temp in celcius")
temp_celcius = int(temp_celcius)
temp_ferenhight = (temp_celcius * 1.8) + 32
print(temp_celcius + "degrees C equals " + temp_ferenhight + " degrees F ")



#some conversion factors
str()
int()
float()
bin()
bool()

#the stuff that goes between the parenthesis is called perameters
#perameter are the values that the functions needs to run

# functions
# functions are a lot like variables
# they have names
# they can be recalled from memory by calling their name
# store information
# variables store values, functions store code
def potato():           # def keyword + name + () + :
    print("potato")     # lines indented underneath are "inside" the function

# functions are not ran when they are defined
# they must be called by their name to run
potato()    # every function call needs ope and closed parenthesis
            # even if it has no parameters

def jump(how_high):
    print(" you jumped " + int(how_high) + " inches!")

jump(14)

def make_a_word(a, b, c, d, e, f, g, h, i, j, k):
    print(a + b + c + d + e + f + g + h + i + j + k)

make_a_word("R", "i", "l", "e", "y")

#functions can have many many lines
def top_ten_games():
    print("1. Seige")
    print("2. Warzone")
    print("3. Minecraft")
    print("4. Fall Guys")
    print("5. Gang Beasts")
    print("6. GTA")
    print("7. Clash of Clans")
    print("8. Geometry Dash")
    print("9. Mario")
    print("10. Fortnite")

#scope: global and local varibles!!
#scope refers to the context in which the varibles was defined
#GLOBAL- defined at no indetation level
#LOCAL- defined inside of a function
    
#global variables can be used anywhere
todd = "cool guy"       #global varible- no indentaion level

#local variables only exist in the scope they were defined
def my_function():
    smith = "not cool guy"  #Local varible- define in a function
    todd = " strange guy"   #Local variables even through it has the same name
    print(todd)             #Prints the local varible todd
    # when you call a varible in a function
    # it searches local varibles first, then global varibles
