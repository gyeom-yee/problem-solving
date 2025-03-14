from itertools import combinations_with_replacement
n, m = map(int, input().split())
arr = sorted(input().split(), key=int)
print('\n'.join(map(" ".join, combinations_with_replacement(arr, m))))