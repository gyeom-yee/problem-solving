from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    queue_li = deque(list(map(int, input().split())))
    level = deque(sorted(queue_li, reverse=True))
    cnt = 0
    while queue_li:
        front = queue_li.popleft()
        m -= 1
        if front == level[0]:
            cnt += 1
            if m < 0:
                print(cnt)
                break
            level.popleft()
        else:
            queue_li.append(front)
            if m < 0:
                m += len(queue_li)