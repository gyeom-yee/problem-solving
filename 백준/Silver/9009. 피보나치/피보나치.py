import sys
from itertools import combinations
input = sys.stdin.readline

T = int(input())

dp = [0, 1]+[0]*44
for i in range(2, 46):
    dp[i] = dp[i-1] + dp[i-2]

for _ in range(T):
    num = int(input())
    result = []
    if num in dp: print(num)
    else:
        for j in dp[:1:-1]:
            if num - j >= 0:
                result.append(j)
                num -= j
        print(" ".join(map(str, result[::-1])))