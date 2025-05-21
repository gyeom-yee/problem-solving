a, b, c = map(int, input().split())
s = [0]*100
for _ in range(3):
    start, end = map(int, input().split())
    for i in range(start, end):
        s[i-1] += 1
print(s.count(1)*a + s.count(2)*2*b + s.count(3)*3*c)