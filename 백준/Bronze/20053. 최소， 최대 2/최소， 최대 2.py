import sys
input = sys.stdin.readline

for _ in range(int(input())):
    input()
    li = list(map(int, input().split()))
    print(min(li), max(li))