exp = input().split('-')
ans = 0

for c in exp[0].split('+'):
    ans += int(c)

for i in exp[1:]:
    for j in i.split('+'):
        ans -= int(j)
print(ans)