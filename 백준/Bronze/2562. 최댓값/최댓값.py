import sys
arr = [int(sys.stdin.readline()) for _ in range(9)]
print(max(arr))
print(max(range(len(arr)), key=lambda i: arr[i])+1)