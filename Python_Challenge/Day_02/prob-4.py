# Remove duplicates from a list without using set()

numbers = input("Enter numbers separated by space: ")

nums = numbers.split()
unique_list = []

for num in nums:
    if num not in unique_list:
        unique_list.append(num)

print("List without duplicates:", unique_list)
