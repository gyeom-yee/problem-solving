import sys
for i in range(1, int(sys.stdin.readline())+1):
    c = sys.stdin.readline().split()
    sys.stdout.write("Case #%d: %d\n" %(i, int(c[0]) + int(c[1])))