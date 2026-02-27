# Write a Python program to reverse a given string without using built-in reverse functions.

a = input("Enter a string: ")

reversed_a = ""
for char in a:
    reversed_a = char + reversed_a

print("Reversed string:", reversed_a)
