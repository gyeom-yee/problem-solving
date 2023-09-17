import sys
arr = sorted([int(x) for x in sys.stdin])
print(sum(arr)//5)
print(arr[2])