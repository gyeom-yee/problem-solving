n = int(input())
flag = 0
for i in range(n//2+1):
    for j in range(n//5+1):
        if 2*i + 5*j == n:
            flag = 1
            print(i+j)
            break
    if flag == 1:
        break
if flag == 0:
    print(-1)