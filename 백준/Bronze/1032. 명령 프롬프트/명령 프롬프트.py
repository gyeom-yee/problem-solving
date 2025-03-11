import sys
n = int(sys.stdin.readline())
arr = [sys.stdin.readline().rstrip() for _ in range(n)]
if n == 1: print(arr[0])
else:
    pattern = []
    flag = 0
    for i in range(len(arr[0])):
        for j in range(n-1):
            flag = arr[j][i]
            if arr[j][i] != arr[j+1][i]:
                flag = '?'
                break
        pattern.append(flag)
    print("".join(pattern))