import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    p = int(input())
    players = []
    for _ in range(p):
        c, name = input().split()
        players.append([int(c), name])
    print(max(players)[1])