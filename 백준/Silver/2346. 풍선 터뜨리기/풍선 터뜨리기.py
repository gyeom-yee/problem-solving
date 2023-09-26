from collections import deque
ans = []
input()
li = list(map(int, input().split()))
dq = deque((val, idx+1) for idx, val in enumerate(li))
while dq:
    v, i = dq.popleft()
    ans.append(str(i))
    if v > 0: dq.rotate(1-v)
    else: dq.rotate(-1*v)
print(" ".join(ans))