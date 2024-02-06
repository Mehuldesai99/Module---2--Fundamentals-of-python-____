# >>> 13.  Write a Python program to count the number of characters (character frequency) in a string 

def char(string):
    freq = {} 

    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

s = input("Enter a string: ")
r = char(s)
for char, freq in r.items():
    print(f"'{char}' : {freq}")
