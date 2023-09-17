import sys
t = int(input())
for _ in range(t):
    c = sum(map(int, sys.stdin.readline().split()))
    print(c)