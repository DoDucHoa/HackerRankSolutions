n = int(input())
counter_dictionary = {}
words_list = []

for i in range(n):
    word = input()
    words_list.append(word)
    # counter_dictionary = {'bcdef': 1, 'abcdefg': 1, 'bcde': 1}
    if word in counter_dictionary:
        # counter_dictionary[bcdef] = 1
        # update dictionary
        counter_dictionary[word] += 1
    else:
        # create a new dictionary with value = 1
        counter_dictionary[word] = 1

print(len(counter_dictionary))
# value of counter_dictionary[bcdef] = 2
# value of counter_dictionary[abcdefg] = 1
print(' '.join([str(counter_dictionary[word]) for word in counter_dictionary]))
