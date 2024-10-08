# Boolean Expression
# Kinda like a mathematical formula
# Can only evaluate to True or False
# Are my shoes tied? = True
# Is 5 > 7 = False
print(5 > 7)

# Comparison operators! == > < >= <=
# Kinda like arithmetic operators! + - * / ** % //

x = 5           # SET x equal to 5, tell it what to be
print(x == 5)   # GET x equals 5, ask a question
# The difference is that we are using one or two equal signs
# This is a PERFECT test question

print(4 >= 2)       # True
print(1993 == 1993) # True
print(-90 < -99)    # False
print(10 != 10)     # False, "bash" "not"


#Boolean Expressions Quiz (Already got on another file)

print("Walrus" == "Walrus")     # == is totally valid for 2 strings




# If Statements
# Evaluate boolean expressions
# Make decisions about which code to run next

# Take a temperature
# Print "<temperature> is hot" if the temperature is >= 80
# Otherwise, print "<temperature> is not hot"
temperature = int(input("What is the temperature?\n"))
# if, boolean expression, :
# sort of like a function, no parenthesis!
if temperature >= 80:        # If th bool evaluates to True, go inside
    print(str(temperature) + " degrees is hot")

else:   # Else takes NO condition and runs when the if above is false
        # Otherwise.....
    print(str(temperature) + " degrees is not hot")

# Compete the activity-
# Create a program that asks for a password
# Print "ACCESS GRANTED" if the password is correct
# Print "ACCESS DENIED" if the password is wrong
# The password is skibidi68
    
password = input("Enter the password\n")
if password == "skibidi68":
    print("Access Granted")
else:
    print("Access Denied")

# Activity 2, electric boogaloo
# Create a five question quiz that prints your score at the end
# Choose any five questions
    
answer_1 = input("What rank is Ricky T in siege")
if answer_1 == "copper":
    print("Correctooo, YUH!")
else:
    print("Not right  :(  (come on bro)")


answer_2 = input("What is my main attack")
if answer_2 == "ying":
    print("Damn right")
else:
    print("Not right  :(  (come on bro)")


answer_3 = input("What is my main defend")
if answer_3 == "doc":
    print("Hells yea, I rock the acog on doc")
else:
    print("Not right  :(  (come on bro)")


answer_4 = input("What is the best reticle")
if answer_4 == "acog":
    print("Only correct answer, no question")
else:
    print("Bro seriously, theres only one right answer, and u didn't get it...    ...Idiot")


answer_5 = input("Is yours truly the best at siege")
if answer_5 == "yes":
    print("Correctooo, YUH!")
else:
    print("Not right  :(  (come on bro)")




