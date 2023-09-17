import sys
input = sys.stdin.readline
for _ in range(int(input())):
    c = input().split()
    sys.stdout.write("%d\n" %(int(c[0]) + int(c[1])))