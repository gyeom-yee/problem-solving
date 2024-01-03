import sys
input = sys.stdin.readline

n = int(input())
arr = sorted([int(input()) for _ in range(n)])
result = 0

for i in range(1, len(arr)+1):
    result += abs(arr[i-1]-i)
print(result)