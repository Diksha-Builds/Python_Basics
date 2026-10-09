''' 
    #
    *   *
    #   #   #
    *   *   *   *
    #   #   #   #   #
'''

row = int(input("Enter number of rows : "))
col = int(input("Enter number of columns : "))

for i in range(row):
    for j in range(col):
        if(i >= j):
            if(i % 2 == 0):
                print("* \t", end=" ")
            else:
                print("# \t", end=" ")
    print()