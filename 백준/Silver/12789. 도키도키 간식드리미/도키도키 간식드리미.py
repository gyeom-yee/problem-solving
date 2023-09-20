n = int(input())
li = list(map(int, input().split()))
ans = []
stk = []
for i in range(1, n+1):
    if i in li:
        while li[0] != i:
            stk.append(li.pop(0))
        ans.append(li.pop(0))
    else:
        ans.append(stk.pop())
print("Nice" if ans == sorted(ans) else "Sad")