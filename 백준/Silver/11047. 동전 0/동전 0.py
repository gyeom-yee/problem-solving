import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)

cnt = 0
for coin in coins:
    tmp = k//coin
    if tmp == 0:
        continue
    else:
        cnt += tmp
        k%=coin
print(cnt)