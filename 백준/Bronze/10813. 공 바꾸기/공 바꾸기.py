import sys
n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    i -= 1; j -= 1
    arr[i], arr[j] = arr[j], arr[i]
print(*arr)