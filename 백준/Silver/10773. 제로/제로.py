import sys
stk = []
for _ in range(int(input())):
    n = int(sys.stdin.readline())
    if n == 0: stk.pop()
    else: stk.append(n)
print(sum(stk))