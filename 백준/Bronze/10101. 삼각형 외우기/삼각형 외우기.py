import sys
d = [int(sys.stdin.readline()) for _ in range(3)]
d_len = len(set(d))
if sum(d) != 180:
    print("Error")
elif d_len == 3:
    print("Scalene")
elif d_len == 2:
    print("Isosceles")
elif d_len == 1:
    print("Equilateral")