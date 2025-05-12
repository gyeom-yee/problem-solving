import sys
data = sys.stdin.read().split()
for s in data[1:]:
    num = "".join(sorted(s, key=int, reverse=True))
    print(int(num[:-1]) + int(num[-1]))