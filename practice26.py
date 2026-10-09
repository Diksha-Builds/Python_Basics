# Enter a name and check if it is palindrome or not

name = input("Enter a name : ")

rev = ""

for i in range(len(name)-1, -1, -1):
    rev = rev + name[i]

if (name == rev):
    print("It is a palindrome")
else:
    print("It is not a palindrome")