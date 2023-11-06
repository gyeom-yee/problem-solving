import sys
input = sys.stdin.readline
n, m = map(int, input().split())
n_arr = [0]+list(map(int, input().split()))
n_sum = [0]*(n+1)
for i in range(1, n+1):
    n_sum[i] = n_sum[i-1] + n_arr[i]
for _ in range(m):
    i, j = map(int, input().split())
    print(n_sum[j]-n_sum[i-1])