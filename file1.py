''' Write a program to read a file and count how many vowels are present in its content '''

def countVowels(filename):
    count = 0

    fobj = open(filename, "r")
    data = fobj.read()
    fobj.close()

    for ch in data:
        if ch in "aeiouAEIOU":
            count += 1

    return count

print("Total no. of vowels are : ",countVowels("demo.txt"))