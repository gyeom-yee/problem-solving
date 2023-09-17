import sys
for x in sys.stdin:
    a, b = map(int, x.split())
    print(a+b)