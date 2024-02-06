# >>> 9.  Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. 

def sum_numbers(a, b, c):
    if a == b or b == c or a == c:
        return 0
    else:
        return a + b + c
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
print(f"Your 1st number is = {a}, 2nd number is = {b}, 3rd number is ={c}")

r = sum_numbers(a, b, c)
print(f"The sum is: {r}")
