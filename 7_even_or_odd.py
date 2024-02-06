# >>> 7.  Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user

def even_odd(num):
    if num % 2 == 0:
        print(f"{num} is even number.")
    else:
        print(f"{num} is odd number.")

number = int(input("Enter a number: "))
even_odd(number)

