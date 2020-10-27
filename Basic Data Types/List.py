def execute(inputCommand):
    command = inputCommand.strip().split("\n")
    myList = []
    for line in command[1:]:
        action = line.split()
        if action[0] == "insert":
            myList.insert(int(action[1]), int(action[2]))
        elif action[0] == "remove":
            myList.remove(int(action[1]))
        elif action[0] == "append":
            myList.append(int(action[1]))
        elif action[0] == "sort":
            myList.sort()
        elif action[0] == "pop":
            myList.pop()
        elif action[0] == "reverse":
            myList.reverse()
        elif action[0] == "print":
            print(myList)


if __name__ == '__main__':
    N = int(input())
    input_list = [str(N)]
    for _ in range(N):
        s = input().strip()
        input_list.append(s)
    input_string = "\n".join(input_list)
    execute(input_string)

