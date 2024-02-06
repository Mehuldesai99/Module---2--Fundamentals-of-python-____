# >>> 12. Write a Python program to calculate the length of a string. 

s = input("Enter a string: ")
count = 0

for char in s:
    count += 1
    print(char)

print("Total characters:", count)