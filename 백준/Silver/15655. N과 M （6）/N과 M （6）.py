from itertools import combinations
n, m = map(int, input().split())
arr = sorted(input().split(), key=int)
print("\n".join(map(' '.join, combinations(arr, m))))