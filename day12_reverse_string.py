# Day 12 - String Processing
# Reverse a string without using built-in reverse functions

text = input("Enter a string: ")

reversed_text = ""

# Traverse the string from the last character to the first
for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]

print("\nOriginal String:", text)
print("Reversed String:", reversed_text)