a,b,c = map(int, input().split())
score = 0

if a == b == c:
    score = 10000+a*1000
elif a == b or a == c:
    score = 1000+a*100
elif b == c:
    score = 1000+c*100
else:
    score = max(a,b,c) * 100
print(score)