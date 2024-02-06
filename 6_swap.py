# >>> 6.  Write python program that swap two number with temp variable and without temp variable.

# swap two number with temp variable 

print(">>>WITH TEMP VARIABLE<<<")
num1=int(input("Enter 1st number = " ))
num2=int(input("Enter 2nd number = " ))
def swap_temp(num1, num2):
    print(f"Your 1st number is = {num1}, 2nd number is = {num2}")
    
    temp = num1 
    num1 = num2
    num2 = temp
    
    print(f"\nswapping with temp variable\n1st number is  = {num1},\n2nd number is = {num2}\n")

swap_temp(num1, num2)

# swap two number without temp variable

print(">>>WITHOUT TEMP VARIABLE<<<")
num1 = int(input("Enter 1st number = "))
num2 = int(input("Enter 2nd number = "))

def swap(num1, num2):  
    print(f"Your 1st number is = {num1}, 2nd number is = {num2}")
    
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    
    print(f"\nSwapping without temp variable\n1st number is  = {num1},\n2nd number is = {num2}")

swap(num1, num2)



