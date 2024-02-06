#>>> 21. Write a Python function to reverses a string if its length is a multiple of 4.

def reverse(str):
    if len(str) % 4 == 0:
        return str[::-1] 
    else:
        return str  

string = input("Enter string: ")
r = reverse(string)
print("Result:", r)

