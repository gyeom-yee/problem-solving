import sys

def cantor(n):
    if n <= 1: return "-"
    return cantor(n//3) + " " * (n//3) + cantor(n//3)

for x in sys.stdin:
    print(cantor(3**int(x)))