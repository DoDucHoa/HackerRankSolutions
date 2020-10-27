from itertools import combinations

# print list(combinations(['a', 'a', 'c', 'd'], 2))

n, l, k = int(input()), input().strip().split(' '), int(input())

count = 0.0
list_count = 0.0

for i in combinations(l, k):
    list_count += 1
    if 'a' in i:
        count += 1

print("%.3f" % (count / list_count))