def runner_up_score(arr):
    # turn to list
    number_list = list(arr)
    # find max score
    maximal_score = max(number_list)
    # find second max score
    runner_up = max([score for score in number_list if score != maximal_score])
    print(runner_up)


if __name__ == '__main__':
    n = int(input())
    # split elements by space and add to list
    # input: 3 4 5 6
    # result: [3,4,5,6]
    arr = map(int, input().split())
    runner_up_score(arr)
