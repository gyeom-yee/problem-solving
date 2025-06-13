import sys
input = sys.stdin.readline

for _ in range(int(input())):
    arr = sorted(list(map(int, input().split())), reverse=True)
    print(arr[2])
