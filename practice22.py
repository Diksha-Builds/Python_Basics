numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a list of 10 numbers and display the sum of last 4 elements
print("Sum of last 4 digits : ",sum(numbers[-4:]))

# Remove the items from the list located at 2nd and 5th position
numbers.pop(1)
numbers.pop(3)
print(numbers)

# Print the difference between highest and smallest number of the list
print("Difference between highest and smallest number : ",numbers[-1]-numbers[0])

# Append a new element in the list which is half of the item located at the third position in the list
half = numbers[2]/2
numbers.append(half)
print(numbers)