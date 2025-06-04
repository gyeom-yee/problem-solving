import sys
input = sys.stdin.readline
n, m = map(int, input().split())
res = list(map(str, range(1, n+1)))

for _ in range(m):
    i, j, k = map(int, input().split())
    res[i-1:j] = res[k-1:j]+res[i-1:k-1]
print(" ".join(res))
