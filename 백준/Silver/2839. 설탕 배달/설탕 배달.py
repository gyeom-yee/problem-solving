n = int(input())
li = []
for i in range(n//5+1):
    for j in range(n//3+1):
        if 5*i + 3*j == n:
            li.append(i+j)
print(-1 if li == [] else min(li))