def free_shipping(status, purchase, age, consent):
    if (status == True or purchase >= 25) and (age >= 18 or consent == True):
        print("You have free shipping!")
    else:
        print("Ineligible for free shipping")

s = False
p = 100
a = 80
c = False

free_shipping(s, p, a, c)