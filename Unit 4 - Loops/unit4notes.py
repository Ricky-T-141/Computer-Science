# Python has four types of collections
# Tuple
# Set
# List
# Dictionary

# Today, we are going to focus on lists
# A list is a way to store more than one value in a single variable
# Those values in the lists are called ITEMS
# ITEMS can be accessed by their index (position in the list)
# INDEX                             0                1              2               3
best_elden_ring_weapons = ["Blasphemous Blade", "Moonveil", "Rivers of Blood", "Iron Ball", "Bloodhound's Fang"]

# INDEX         0     1     2     3
best_years = [1776, 1985, 1994, 1957]

# Print the index of the value in the list
print(best_years.index(1985))

# Print the best elden ring weapon
print(best_elden_ring_weapons[0])

# Print the worst of he best elden ring weapon
print(best_elden_ring_weapons[len(best_elden_ring_weapons)-1])

# List items can be changed!
best_elden_ring_weapons[3] = "Spiked Fist"
print(best_elden_ring_weapons)

# Remove the last item in the list by its position in the list
# The .pop() function removes an item in a list by its position in the list
best_elden_ring_weapons.pop(4)
print(best_elden_ring_weapons)

# Remove an item by its value
best_elden_ring_weapons.remove("Moonveil")
print(best_elden_ring_weapons)

# Add a new item to the end of a list
best_elden_ring_weapons.append("Mohgwyn's Sacred Spear")
print(best_elden_ring_weapons)

import random
numbers = [random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100)]
print(numbers)
print(max(numbers))
print(min(numbers))
numbers.sort()
print(numbers)
# Strings are lists!
# Strings are just a list of characters
word = "potato"
print(word[0])






# For loops
# This is a BIG deal
# For loops allow the programmer to REPEAT, or what we call LOOP

# Write a program that prints the numbers one through ten

# for <temp var> in <list>:

#  range(0,10) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(0,10):       # 0 is the START value, 10 is the STOP value
    print(i)
    print("yo")

top_foods = ["Eggs Benedict", "Fried Chicken", "Mac n Cheese"]
# "Go through every food in top foods"
# Repeats everything in the for loop for each item in the list
# Where food equals the current item
for food in top_foods:
    print(food)


# Practice
    
groceries = ["milk", "eggs", "bread", "butter", "apples"]


added_item = input("What is something you purchased at the store?\n")

for items in groceries:
    if items == added_item:
        print(added_item + "crossed off the list")
        groceries.remove(added_item)
    
    print(items)


# Create a list of five random numbers from 0-100
# Use a for loop to find the sum of those numbers
    
five_numbers = [random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100)]
for number in five_numbers:
    sum = number + number + number + number + number
    print(sum)