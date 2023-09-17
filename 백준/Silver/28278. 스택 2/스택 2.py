import sys
stk = []
for _ in range(int(input())):
    m = list(map(int, sys.stdin.readline().split()))
    if len(m) == 1:
        if m[0] == 2:
            print(stk.pop() if stk != [] else -1)
        elif m[0] == 3:
            print(len(stk))
        elif m[0] == 4:
            print(1 if stk == [] else 0)
        elif m[0] == 5:
            print(stk[-1] if stk != [] else -1)
    else:
        stk.append(m[1])