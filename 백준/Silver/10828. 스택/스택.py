import sys
res = []
stk = []
li = sys.stdin.readlines()[1:]
for x in li:
    command = x.split()[0]
    if command == "push":
        stk.append(x.split()[1])
    elif command == "pop":
        res.append(stk.pop() if stk else '-1')
    elif command == "size":
        res.append(str(len(stk)))
    elif command == "empty":
        res.append('0' if stk else '1')
    elif command == "top":
        res.append(stk[-1] if stk else '-1')
sys.stdout.write("\n".join(res))