# Write a Python program to count the number of vowels in a given string.
a = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in a:
    if char in vowels:
        count += 1

print("Number of vowels:", count)
