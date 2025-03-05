import sys
input = sys.stdin.readline

t = int(input())
result = []
for _ in range(t):
    n = int(input())
    cloth = [list(input().split()) for _ in range(n)]
    cnt = 1
    weardict = {}
    for q in cloth:
        if q[1] in weardict:
            weardict[q[1]] += 1
        else:
            weardict[q[1]] = 1
    for i in weardict:
        cnt *= weardict[i] + 1
    print(cnt-1)