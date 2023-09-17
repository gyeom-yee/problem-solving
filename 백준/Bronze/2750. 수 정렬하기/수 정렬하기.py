import sys
arr = []
idx = 0
for _ in range(int(input())):
    n = int(sys.stdin.readline())
    for i in range(len(arr)):
        if n > arr[i]: idx = i+1
        elif n < arr[0]:
            idx = 0
            break
    arr.insert(idx, n)
print(*arr, sep='\n')