import sys
for _ in range(int(input())):
    ps = sys.stdin.readline().rstrip()
    stk = []
    for x in ps:
        if stk==[]: stk.append(x)
        elif stk[-1]=="(" and x==")":
            stk.pop()
        else: stk.append(x)
    print("YES" if stk==[] else "NO")