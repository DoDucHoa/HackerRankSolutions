def average(array):
    set_number = set(arr)
    total_distinct = len(set_number)
    sum = 0
    for i in set_number:
        sum += i
    return sum / total_distinct


if __name__ == '__main__':
    n = int(input())
    # map(function, iterable)
    arr = list(map(int, input().split())) # change all input() to int()
    result = average(arr)
    print(result)

