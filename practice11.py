# Python examples for common string functions

# Sample string
text = "    Welcome to IMCC!    "

# 1. Strip spaces from both ends
print("Remove spaces",text.split())

# 2. Convert to uppercase
print("Upper case : ",text.upper())

# 3. Convert to lowercase
print("Lower case : ",text.lower())

# 4. Capitalize the first letter
text = text.strip()
print("Capitalize First Letter : ",text.upper())

# 5. Title case (capitalize each word)
print(text.title())

# 6. Count occurences of a substring
print("Letter C occurs ",text.count("C"), "times in text")

# 7. Find the position of a substring (-1 if not found)
print("position of IMCC in text is ",text.find("IMCC"))

# 8. Replace a substring
print(text.replace("IMCC", "Python Magic"))

# 9. Check if string starts or ends with certain substring
print(text.startswith("  We"))
print(text.endswith("!     "))

# 10. Split string into list by a delimiter
print("Simple split",text.split())

# 11. Join a list of strings with a separator
words = ["Python", "is", "fun"]
print(" ".join(words))