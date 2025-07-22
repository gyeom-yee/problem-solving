n = int(input())
arr = list(map(int, input().split()))

y = 0
m = 0

for s in arr:
    y += (s//30+1)*10
    m += (s//60+1)*15

if y > m:
    print('M', m)
elif y == m:
    print('Y M', y)
else:
    print('Y', y)