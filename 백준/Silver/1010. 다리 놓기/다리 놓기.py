import sys
for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    a, b = 1, 1
    for i in range(m,m-n,-1): a *= i
    for j in range(1, n+1): b *= j
    print(a//b)