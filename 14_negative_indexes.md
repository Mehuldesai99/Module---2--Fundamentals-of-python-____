>>> 14. What are negative indexes and why are they used?

>> Negative indexes in programming languages like Python refer to accessing elements from the end of a sequence or container (such as a list, string, or tuple) rather than from the beginning. In Python, negative indexing allows you to access elements from the end of the sequence by using negative numbers as indices.

For instance, in a list or string:

* The last element has an index of -1.
* The second-to-last element has an index of -2.
* And so on, with subsequent elements counted backward using negative numbers.

1). Accessing elements from the end :  It provides a convenient way to access elements from the end of a sequence without needing to know its length explicitly. For example, if you want to access the last element of a list without knowing its length, you can use -1 as the index.

For example:
my_list = [1, 2, 3, 4, 5]
last_element = my_list[-1]  # Accessing the last element of the list

2). Slicing from the end: Negative indexing is useful for slicing operations when you want to retrieve a portion of the sequence from the end. 

For example:
my_string = "Hello, World!"
last_five_chars = my_string[-5:]  # Getting the last five characters of the string

3). Convenience in reverse traversal: It facilitates traversing a sequence in reverse order by using negative indexing in loops or iteration constructs. 

For example:
my_list = [1, 2, 3, 4, 5]
for i in range(-1, -len(my_list) - 1, -1):
    print(my_list[i])  # Prints elements in reverse order

>> Negative indexes offer flexibility, especially when dealing with sequences where the length is unknown or when accessing elements from the end without explicitly counting from the beginning of the sequence. They provide a convenient way to work with sequences in reverse or access elements near the end without needing to know the sequence's length beforehand.

