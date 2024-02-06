# >>> 23.  Write a Python function to insert a string in the middle of a string.

def insert_middle(o_str, i_str):
    middle_index = len(o_str) // 2

    modified_str = o_str [:middle_index] + " " + i_str + o_str[middle_index:]

    return modified_str

o_str = input("Enter string : ")
i_str= input("Insert middle: ")

r= insert_middle(o_str, i_str)
print(f"update string : {r}")
