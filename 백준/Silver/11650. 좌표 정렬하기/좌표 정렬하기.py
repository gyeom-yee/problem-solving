import sys
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(int(input()))]
arr.sort()
for i in arr: print(" ".join(map(str, i)))