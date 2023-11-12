n, k = map(int, input().split())
arr = list(map(int, input().split()))
res = []
n_sum = [0]
tmp = 0

for x in arr:
    tmp += x
    n_sum.append(tmp)

for i in range(n-k+1):
    res.append(n_sum[i+k]-n_sum[i])

print(max(res))