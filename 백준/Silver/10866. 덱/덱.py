from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
dq = deque()

for _ in range(n):
    s = input().split()
    if s[0] == 'push_front':
        dq.appendleft(int(s[1]))
    elif s[0] == 'push_back':
        dq.append(int(s[1]))
    elif s[0] == 'pop_front':
        print(dq.popleft() if dq else -1)
    elif s[0] == 'pop_back':
        print(dq.pop() if dq else -1)
    elif s[0] == 'size':
        print(len(dq))
    elif s[0] == 'empty':
        print(0 if dq else 1)
    elif s[0] == 'front':
        print(dq[0] if dq else -1)
    elif s[0] == 'back':
        print(dq[-1] if dq else -1)