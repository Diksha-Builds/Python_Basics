# Print sum of first even 10 numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
sum = 0

for i in range(20):
    if(numbers[i] % 2 == 0):
        sum = sum + numbers[i]

print("Sum of first 10 even numbers", sum)

# Accept two values S and N. Print square of first N numbers starting from S
S = int(input("Enter starting value : "))
N = int(input("Enter ending value : "))

sqr = 0

for i in range(S, N):
    srq = numbers[i] * numbers[i]
    print(srq)

# Reverse the accepted string
text = input("Enter string : ")

for i in range(-1):
    print(text, end="")
    i-=1