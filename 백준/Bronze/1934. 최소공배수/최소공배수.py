import sys
for i in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())
    x, y = a, b

    while a%b != 0:
        a, b = b, a%b

    print(x*y//b)