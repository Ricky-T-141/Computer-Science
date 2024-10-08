print("Answer all in lowercase")
answer_1 = input("What rank is Ricky T in Tom Clancy's Rainbow Six Siege?\n")
if answer_1 == "copper":
    print("Correctooo, YUH!")
    x = 1
else:
    print("Not right  :(  (come on bro)")
    x = 0


answer_2 = input("What is my main attack in Siege?\n")
if answer_2 == "ying":
    print("Damn right")
    x = x + 1
else:
    print("No bru, its ying with her candela grenades")


answer_3 = input("What is my main defend in Siege?\n")
if answer_3 == "doc":
    print("Hells yea, I rock the acog on doc")
    x = x + 1
else:
    print("Incorrect, it be doc with that beautiful stim pistol")


answer_4 = input("What is the best reticle?\n")
if answer_4 == "acog":
    print("Only correct answer, no question")
    x = x + 1
else:
    print("Bro seriously, theres only one right answer, and u didn't get it...    ...Idiot")


answer_5 = input("Is yours truly the best at siege?\n")
if answer_5 == "yes":
    print("Of course I am <3")
    x = x + 1
else:
    print("Ok bro just start again if ur gettin the easiest question wrong; just embarrassing at this point")

print("Total score: " + str(x) + "/5")