num1 = int(input("Enter a number : "))
rev = 0
num2 = num1

while(num1 > 0):
    rev = rev*10 + (num1%10)
    num1 = num1 // 10

if(num2 == rev):
    print("Number is a palindrome")
else:
    print("Number is not a palindrome")