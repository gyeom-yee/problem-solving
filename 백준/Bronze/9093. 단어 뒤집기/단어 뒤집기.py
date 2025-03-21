import sys
t = int(input())
for _ in range(t):
    s = [w[::-1] for w in sys.stdin.readline().split()]
    print(" ".join(s))