import sys
input = sys.stdin.readline
n, m = map(int, input().split())
sites = dict()
for _ in range(n):
    key, val = input().split()
    sites[key] = val
for _ in range(m):
    print(sites[input().rstrip()])