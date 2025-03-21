import sys
t = int(input())
for _ in range(t):
    s = sys.stdin.readline()[::-1].split()[::-1]
    print(" ".join(s))