# >>> 16. Write a Python program to count the occurrences of each word in a given sentence 

def count_word(sent):
    word = sent.split()
    w_count = {}

    for word in word:
        word = word.strip(" , : ; . ! ? ").lower()

        if word in w_count:
            w_count[word] += 1
        else:
            w_count[word] = 1

    return w_count

sentence = input("Enter a sentence: ")

w_occurrences = count_word(sentence)

for word, count in w_occurrences.items():
    print(f"'{word}': {count}")
