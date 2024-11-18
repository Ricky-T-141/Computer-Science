# Dictionary is a type of collection like list
# A list is a collection of items in a sequence
# A dictionary is different
# Dictionaries store data in key-value pairs
# You can retreive data quickly by using a unique key
# Instead of retreiving it by index (position)

# Example
# Lists use brackets, dictionaries use braces
rickyT = {
    "name": "Riley",
    "age": 18,
    "city": "Saint Michael",
    "siblings": "1, brother",
    "height": 5.8
}
# Each key must be unique

# Retreiving values from a dictionary

print(rickyT["age"])

# .get allows you to retreive a value without erroring
# When the key doesen't exist
# The second parameter is what is given if value is not found
print(rickyT.get("height"))
print(rickyT.get("weight", "fortnite"))

# You can add values to a dictionary

rickyT["country"] = "USA"

# You can modify values
rickyT["age"] = 19

print(rickyT)


# Remove entries
rickyT.pop("siblings")

# Iterate through a dictionary using a for loop 

for key, value in rickyT.items():
    print(key + ": " + str(value))

# Dictionary functions
print(rickyT.keys())    # Returns all keys
print(rickyT.values())  # Returns all values
print(rickyT.items())   # Returns all pairs
print(rickyT.clear())   # Removes all items from the dictionary




Grades = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "C",
    "David": "A",
    "Eve": "B"
}

student = {
    "name": "Alice",
    "age": 16,
    "grade": "A"
}


student["grade"] = "A+"
print(student)



best_movies = {
    "Black Hawk Down": 2001,
    "The Dark Knight Rises": 2012,
    "Interstellar": 2014
}

best_movies["Inception"] = 2010



fruits = {
    "apple": "$115",
    "orange": "$500",
    "pear": "$0.50",
    "bannana": "Priceless",
    "papaya": "10000"
}

fruits.pop("orange")
print(fruits)




