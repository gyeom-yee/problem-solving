import sys
n, m = map(int, input().split())
arr = [i for i in range(1,n+1)]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    i-=1
    arr[i:j] = reversed(arr[i:j])
print(*arr)