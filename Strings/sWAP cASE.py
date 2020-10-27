def swap_single_char(single_char):
    if single_char.islower():
        return single_char.upper()
    else:
        return single_char.lower()


def swap_case(s):
    return ''.join([swap_single_char(single_char) for single_char in s])


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
