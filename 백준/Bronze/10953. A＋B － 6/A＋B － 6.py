import sys
arr = sys.stdin.readlines()
for t in arr[1:]:
    t.split()
    a, b = map(int, t.split(','))
    print(a+b)