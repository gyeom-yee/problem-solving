import sys
from collections import deque
dq = deque()
res = []
li = sys.stdin.readlines()[1:]
for x in li:
    command = x.split()[0]
    if command == "push":
        dq.append(x.split()[1])
    elif command == "pop":
        res.append(dq.popleft() if dq else '-1')
    elif command == "size":
        res.append(str(len(dq)))
    elif command == "empty":
        res.append('0' if dq else '1')
    elif command == "front":
        res.append(dq[0] if dq else '-1')
    elif command == "back":
        res.append(dq[-1] if dq else '-1')
sys.stdout.write("\n".join(res))