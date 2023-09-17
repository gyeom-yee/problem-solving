import sys
for x in sys.stdin:
    a, b = map(int, x.split())
    if a == b == 0:
        sys.exit()
    if b%a == 0:
        print("factor")
    elif a%b == 0:
        print("multiple")
    else:
        print("neither")