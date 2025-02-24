from itertools import permutations
n, m = map(int, input().split())
n_li = sorted(list(input().split()), key=int)
print('\n'.join(map(" ".join, permutations(n_li, m))))