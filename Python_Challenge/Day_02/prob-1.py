# Find the second largest number in a list without using sort()
nums = list(map(int, input("Enter numbers separated by space: ").split()))

largest = second = float('-inf')

for num in nums:
    if num > largest:
        second = largest
        largest = num
    elif largest > num > second:
        second = num

print("Second Largest:", second)
