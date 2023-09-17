import sys
for _ in range(int(input())):
    R, S = sys.stdin.readline().split()
    for i in S:
        print(i*int(R), end='')
    print()