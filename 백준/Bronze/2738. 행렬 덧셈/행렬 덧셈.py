import sys
arr_a = []
arr_b = []
n, m = map(int, input().split())
for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    arr_a.append(row)
for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    arr_b.append(row)
for i in range(n):
    for j in range(m):
        print(arr_a[i][j] + arr_b[i][j], end=" ")
    print()