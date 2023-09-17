import sys
x = int(input())
n = int(input())

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    x -= a*b
print("Yes" if x == 0 else "No")