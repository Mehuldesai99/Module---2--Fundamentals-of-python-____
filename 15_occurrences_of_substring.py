# >>> 15.  Write a Python program to count occurrences of a substring in a string. 

def count_occu(m_string, s_string):
    count = m_string.count(s_string)
    return count

m_str = input("Enter a string : ")
s_str = input("Enter substring to count : ")

occurrences = count_occu(m_str, s_str)
print(f"'{s_str}' occurs {occurrences} times in the string.")
