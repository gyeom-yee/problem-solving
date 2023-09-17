import sys
n, m = map(int, input().split())
s = []
cnt = 0
for i in range(n):
    s.append(sys.stdin.readline().rstrip())
s = set(s)
for j in range(m):
    if sys.stdin.readline().rstrip() in s:
        cnt += 1
print(cnt)