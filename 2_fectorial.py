# >>> 2.  Write a Python program to get the Factorial number of given number

num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
        factorial *= i

print(f"Factorial number is {factorial}.")
