N, M = map(int, input().split())

if N == 0:
    print(0)
else:
    w_li = list(map(int, input().split()))
    tmp = 0
    res = 1 #if로 카운팅 안되는 마지막 상자
    for i in range(N-1, -1, -1):
        tmp += w_li[i]
        if tmp > M:
            res += 1
            tmp = w_li[i]
    print(res)