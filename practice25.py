# Create a heterogenous list of numbers and names. Split the list from highest number

list1 = [1, "Diksha", 3, "Pranjali", 9, "Rutuja", 7, 5, "Sakshi", 2, "Trupti"]
max = 0

for i in range(len(list1)):
    if(isinstance(list1[i], int)):
        if(list1[i] > max):
            max = list1[i]

parts = list1.index(max)

part1 = list1[:parts]
part2 = list1[parts:]

print(part1)
print(part2)