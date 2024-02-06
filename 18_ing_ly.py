# >>> 18. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged. 

def add_ing_ly(str):
    if len(str) < 3:
        return str
    elif str[-3:] == 'ing':
        return str + 'ly'
    else:
        return str + 'ing'
s = input("Enter a string: ")
r = add_ing_ly(s)
print("Result:", r)
