def create_hash(integer_list):
    my_tuples = tuple(integer_list)
    print(hash(my_tuples))


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    create_hash(integer_list)
