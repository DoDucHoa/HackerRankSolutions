def count_substring(string, sub_string):
    sum = 0
    for i in range(0, len(string)):
        # string = 'hoado'
        # string[0:2] = 'ho'
        if string[i: i + len(sub_string)] == sub_string:
            sum += 1
    return sum


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    result = count_substring(string, sub_string)
    print(result)

