# >>> 8.  Write a Python program to test whether a passed letter is a vowel or not. 

def vowel(letter):
    vowels = " a e i o u A E I O U "
    if letter in vowels:
        print(f"{letter} is a vowel letter.")
    else:
        print(f"{letter} is not a vowel letter.")

char = input("Enter a character : ")

if len(char) == 1:
    vowel(char)
else:
    print("Please enter a single character.")
