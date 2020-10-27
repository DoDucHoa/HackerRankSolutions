def merge_the_tools(string, k):
    # string = AABCAAADA , k = 3
    num_subsegments = int(len(string) / k)
    # num_subsegments = 3
    for i in range(num_subsegments):
        # slice the string
        # index * number of char want to slice (k)
        # i = 0 => 0 * 1: 1 * 3 => [0: 3]
        # i = 1 => 1 * 3: 2 * 3 => [3: 6]
        t = string[i * k: (i + 1) * k]
        # t = 'AAB'
        u = '' # initial new u
        for c in t:
            if c not in u:
                # string addition
                u += c
        print(u)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
