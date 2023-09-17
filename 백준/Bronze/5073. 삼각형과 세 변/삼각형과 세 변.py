import sys
while True:
    s = list(map(int, sys.stdin.readline().split()))
    if sum(s) == 0:
        break
    s_len = len(set(s))
    s.sort()
    if s[2] >= s[0]+s[1]:
        print("Invalid")
    elif s_len == 1:
        print("Equilateral")
    elif s_len == 2:
        print("Isosceles")
    elif s_len == 3:
        print("Scalene")