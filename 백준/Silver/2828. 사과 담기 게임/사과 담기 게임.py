import sys
input = sys.stdin.readline

N, M = map(int, input().split())
J = int(input())
basket_start = 1
basket_end = M
res = 0

for _ in range(J):
    apple = int(input())
    if basket_start <= apple <= basket_end:
        continue
    elif basket_start > apple:
        tmp = basket_start-apple
        res += tmp
        basket_start -= tmp
        basket_end -= tmp
    elif basket_end < apple:
        tmp = apple - basket_end
        res += tmp
        basket_start += tmp
        basket_end += tmp
print(res)