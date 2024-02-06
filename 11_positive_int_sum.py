# >>> 11.  Write a python program to sum of the first n positive integers.

def sum(n):
    if n <= 0:
        return "Please enter a positive integer."
    else:
        sum_n = (n * (n + 1)) // 2
        return sum_n
n = int(input("Enter a positive integer: "))
result = sum(n)
print("first", n, "positive integers summation is", result)
