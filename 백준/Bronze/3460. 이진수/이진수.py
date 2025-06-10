import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = format(int(input()), 'b')[::-1]
    print(" ".join(str(i) for i in range(len(n)) if n[i] == '1'))