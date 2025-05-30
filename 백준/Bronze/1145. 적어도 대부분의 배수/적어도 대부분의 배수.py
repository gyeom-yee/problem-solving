from itertools import combinations
import math
arr = list(map(int, input().split()))
res = 10**13
for tup in combinations(arr, 3):
    tmp = math.lcm(*tup)
    if tmp < res:
        res = tmp
print(res)