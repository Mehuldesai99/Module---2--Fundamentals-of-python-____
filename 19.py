
# >>> 19Write a Python program to find the first appearance of the substring
# 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
# whole 'not'...'poor' substring with 'good'. Return the resulting string.


def replace_not_poor(input_string):
    index_not = input_string.find('not')
    index_poor = input_string.find('poor')
    if index_not != -1 and index_poor != -1 and index_not < index_poor:
        result_string = input_string[:index_not] + 'good' + input_string[index_poor + 4:]
    else:
        result_string = input_string

    return result_string

given_string = "The weather is not too poor today, but it was not so good yesterday."
result = replace_not_poor(given_string)
print(result)
