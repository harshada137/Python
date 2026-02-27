# Write a Python program to find the largest among three numbers entered by the user.

num1 = int(input("Enter a Number: "))
num2 = int(input("Enter a Number: "))
num3 = int(input("Enter a Number: "))

print(num1, num2, num3)

if num1 > num2 and num1> num3:
    print(f"{num1} Is greatest of all")

elif num2 > num3 and num2 > num3:
    print(f"{num2} Is greates of all")

elif num3 > num1 and num3 > num2:
    print(f"{num3} Is greatest of all")

else:
    print("All Values are Same")        


