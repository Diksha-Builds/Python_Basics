'''Take a sentence from the user, split it into words, and store them in a list. Print the longest word.'''

text = input("Enter a sentence : ")

words = text.split()

longest = words[0]

for i in words:
    if len(i) > len(longest):
        longest = i

print("Words : ",words)
print("Longest word : ",longest)