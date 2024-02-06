# >>> 10.  Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

def values(a, b):
    return a == b or abs(a - b) == 5 or a + b == 5

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
print(f"Your 1st number is = {a}, 2nd number is = {b}")

r = values(a, b)
print(f"The result is: {r}")
