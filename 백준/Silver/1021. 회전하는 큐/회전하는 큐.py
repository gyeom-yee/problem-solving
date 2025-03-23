from collections import deque
n, m = map(int, input().split())
positions = list(map(int, input().split()))
dq = deque(range(1, n+1))
cnt = 0

for position in positions:
    p_idx = dq.index(position)
    if p_idx > len(dq)-p_idx:
        cnt += len(dq)-p_idx
        dq.rotate(len(dq)-p_idx)
    else:
        cnt += p_idx
        dq.rotate(-p_idx)
    dq.popleft()
print(cnt)