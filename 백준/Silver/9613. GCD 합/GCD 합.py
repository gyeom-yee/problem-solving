import sys
from itertools import combinations
input = sys.stdin.readline

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

n = int(input())
for _ in range(n):
    result = 0
    arr = list(map(int, input().split()))[1:]
    for twin in combinations(arr, 2):
        result += gcd(twin[0], twin[1])
    print(result)