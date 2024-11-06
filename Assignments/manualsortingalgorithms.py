# Bubble Sort

num = [34, 7, 23, 32, 5, 62]
print(num)
def bubble_sort(numbers):   #Takes the list as a parameter
    # Create a variable for how many steps we are taking, start at zero
    steps = 0

    # Check if the list is sorted as many times as their are list items
    for j in range(0, len(numbers)-1):
        # Iterate through every item in the list
        for i in range(0, len(numbers) - 1):
            # Check i the current list item is greater than the next list item
            if numbers[i] > numbers[i + 1]:
                # Swap their values
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                # Increase number of steps
                steps += 1
                
    print(numbers) 
    print("Completed in " + str(steps) + " steps.")
bubble_sort(num)




# Quick Sort

numb = [53, 63, 6, 30, 8, 87, 104]
print(numb)
def quick_sort(n):
    # Set pivot as the last number
    pivot = n[-1]

    # l First number from the left that is LARGER
    lPos = 0        # Set to default
    # r First number from the right that is SMALLER
    rPos = len(n)-1 #Set to default
    for j in range(0,len(n)):
        # Find l
        for i in range(0, len(n)):
            if n[i] > pivot:
                lPos = i
                break 

        # Find r
        for i in range(len(n)-1, -1, -1):
            if n[i] < pivot:
                rPos = i
                break
        
        # Check if l index is greater than r index
        if lPos > rPos:
            # Switch pivot with item from left
            n[lPos], n[-1] = n[-1], n[lPos]
            # Stop sorting
            break
        else:
            # Swap l and r values
            n[lPos], n[rPos] = n[rPos], n[lPos]

    

    print(n)
    
quick_sort(numb)            


            
