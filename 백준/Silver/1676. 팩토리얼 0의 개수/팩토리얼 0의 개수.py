n = int(input())
fact = 1
res = 0
for i in range(1, n+1):
    fact *= i
for t in str(fact)[::-1]:
    if t != '0': break
    res += 1
print(res)