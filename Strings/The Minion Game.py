def minion_game(string):
    # set() => vowels_list = {'a', 'e', ...}
    # auto remove duplicate elements when use set()
    vowels_list = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    consonants = 0
    vowels = 0
    string_length = len(string)

    # enumerate auto indexintg elements in the list
    # ['apple', 'banana', 'cherry']
    # => [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
    for index, character in enumerate(string):
        # string = BANANA
        # 0 B      (index = 0 & character = B)
        # 1 A
        # 2 N ...
        if character in vowels_list:
            # A(1) AN(2) ANA(3) ANAN(4) ANANA(5)
            # A(6) AN(7) ANA(8)
            # A(9)
            vowels += string_length - index
            # 5 8 9
        else:
            consonants += string_length - index

    if vowels == consonants:
        print("Draw")
    elif vowels > consonants:
        print("Kevin {}".format(vowels))
    else:
        print("Stuart {}".format(consonants))


if __name__ == '__main__':
    s = input()
    minion_game(s)
