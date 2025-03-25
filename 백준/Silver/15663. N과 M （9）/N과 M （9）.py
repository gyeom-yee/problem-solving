from itertools import permutations
n, m = map(int, input().split())
arr = sorted(input().split(), key=int)
result = set()

for item in permutations(arr, m):
    s = " ".join(item)
    if s not in result:
        result.add(s)
        print(s)