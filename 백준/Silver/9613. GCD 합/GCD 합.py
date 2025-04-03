import sys
from itertools import combinations, starmap
from math import gcd
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))[1:]
    answer = sum(starmap(gcd, combinations(arr, 2)))
    print(answer)