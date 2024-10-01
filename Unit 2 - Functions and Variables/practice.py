def best_movies_of_all_time():                #Define a new function
    print("Black Hawk Down") 
    print("The Dark Knight Rises")
    print("Interstellar")

def add(x, y):
    print(x + y)

one = int(input("Pick a number"))
two = int(input("Pick another number"))
add(one, two)


x = 4
def my_function():
    global x    #From now on, when I call x, I'm talking about the global version!! Not the local verison...
    x = 5       #Reassigning the global variable x
    print(x)    #Prints 5

print(x)  
my_function()