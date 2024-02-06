# >>> 20.  Write a Python function that takes a list of words and returns the length of the longest one.

def long_word(words):
    if not words:
        return 0
    else:
        return max(len(word) for word in words.split())

word_list = input("Enter multiple words separated by spaces: ")
r = long_word(word_list)
print("Length of long word:", r)

