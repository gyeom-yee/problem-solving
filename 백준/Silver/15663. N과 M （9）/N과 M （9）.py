from itertools import permutations
n, m = map(int, input().split())
arr = input().split()
result = sorted(set(tuple(map(int, item)) for item in permutations(arr, m)))
for item in result:
    print(" ".join(map(str,item)))