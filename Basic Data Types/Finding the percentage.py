def get_percent(query_name, student_marks):
    # marks = [score]
    marks = student_marks[query_name]
    # count_average
    average = (marks[0] + marks[1] + marks[2]) / 3
    # format x.00
    print(format(average, '.2f'))


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        #  input() reads single line of input
        # 'abc 23 34 45'
        # splits it into a list of whitespace separated tokens
        # ['abc', '23', '34', '45']
        # name is assigned first token, line a list of the remaining tokens
        # name = 'abc'
        # line = ['23', '34', '45']
        name, *line = input().split()
        # maps float function onto the list of strings
        # scores = [23.0, 34.0, 45.0]
        scores = list(map(float, line))
        # key = 'name' : value = [scores]
        student_marks[name] = scores
    query_name = input()
    get_percent(query_name, student_marks)
