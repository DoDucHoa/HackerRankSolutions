def find_second_lowest(student_list):
    # compare elements at index = 1 which is score
    # take the min out
    lowest_student = min(student_list, key=lambda x: x[1])
    # if lowest student != second lowest student
    # ignore lowest student and compare second lowest student with
    # other students
    second_lowest_student = min([student for student in student_list if student[1] != lowest_student[1]],
                                key=lambda x: x[1])
    # if lowest student == second lowest student
    # sorted name and print
    # else print second lowest student
    sub_student = sorted([student[0] for student in student_list if student[1] == second_lowest_student[1]])
    print('\n'.join(sub_student))


if __name__ == '__main__':
    student_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_list.append([name, score])
    find_second_lowest(student_list)
