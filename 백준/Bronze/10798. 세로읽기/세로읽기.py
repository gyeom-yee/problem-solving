import sys
arr = []
for _ in range(5):
    arr.append(sys.stdin.readline().rstrip())
for i in range(15):
    for j in range(5):
        if i > len(arr[j])-1: pass
        else: print(arr[j][i], end="")