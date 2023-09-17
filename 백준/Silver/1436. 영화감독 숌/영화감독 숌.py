n = int(input())
cnt = 0
for i in range(666, int(str(n)+"666")+1):
    if str(i).find("666") >= 0:
        cnt += 1
        if cnt == n:
            ans = i
            break
print(ans)