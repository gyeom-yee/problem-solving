import sys
for i in range(1, int(sys.stdin.readline())+1):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #%d: %d + %d = %d" %(i, a, b, a+b))