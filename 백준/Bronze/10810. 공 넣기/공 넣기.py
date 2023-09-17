import sys
n, m = map(int, input().split())
arr = [0 for _ in range(n)]
for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    arr[i-1:j] = [k]*(j-(i-1))
print(*arr)