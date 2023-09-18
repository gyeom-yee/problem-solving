import sys
while True:
    s = sys.stdin.readline().rstrip()
    stk = []
    if s==".":
        break
    else:
        for x in s:
            if x in "()[]":
                if stk==[] or x in "([":
                    stk.append(x)
                elif stk[-1]=="(":
                    if x==")": stk.pop()
                    elif x=="]": break
                elif stk[-1]=="[":
                    if x == "]": stk.pop()
                    elif x == ")": break
    print("no" if stk else "yes")