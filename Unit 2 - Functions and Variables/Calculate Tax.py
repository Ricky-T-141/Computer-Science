def calculate_tax(price, rate):
    print(str(price) * float(rate))
calculate_tax(5, 0.06875)    


def add():
    print("Adding numbers")
    one = input("Pick a number\n-")
    one = int(one)
    two = input("Pick another number\n-")
    two = int(two)
    print(str(one + two))

add()      