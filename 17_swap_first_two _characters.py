# >>> 17.  Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

def swap_char(str1, str2):

    n_str1 = str2[:2] + str1[2:]
    n_str2 = str1[:2] + str2[2:]

    result = n_str1 + ' ' + n_str2
    return result

s1 = input("Enter 1st string : ")
s2 = input("Enter 2nd string : ")
print(f"Your 1st string is'{s1}'and 2nd string is'{s2}'")

swap_str = swap_char(s1, s2)
print(f"swap first two characters: {swap_str}")
