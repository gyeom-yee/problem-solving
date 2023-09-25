import sys
from collections import deque
li = sys.stdin.readlines()[1:]
dq = deque()
ans = []
for x in li:
    commander = x.split()[0]
    if commander == "1":
        dq.appendleft(x.split()[1])
    elif commander == "2":
        dq.append(x.split()[1])
    elif commander == "3":
        ans.append(dq.popleft() if dq else "-1")
    elif commander == "4":
        ans.append(dq.pop() if dq else "-1")
    elif commander == "5":
        ans.append(str(len(dq)))
    elif commander == "6":
        ans.append("0" if dq else "1")
    elif commander == "7":
        ans.append(dq[0] if dq else "-1")
    elif commander == "8":
        ans.append(dq[-1] if dq else "-1")
sys.stdout.write("\n".join(ans))