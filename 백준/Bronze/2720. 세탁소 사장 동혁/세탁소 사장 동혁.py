import sys
coin = [25, 10, 5, 1]
for _ in range(int(input())):
    C = int(sys.stdin.readline())
    arr = []
    for i in coin:
        arr.append(C//i)
        C %= i
    print(*arr)