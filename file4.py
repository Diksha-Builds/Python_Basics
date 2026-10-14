'''
Read a file, split its content into words, and store them in a list.
    1. Print the total number of words.
    2. Print all unique words.
'''

fobj = open("demo.txt", "r")

content = fobj.read()
words = content.split()

print("Total number of words : ",len(words))

unique = set(words)
print("Unique words : ",unique)

fobj.close()