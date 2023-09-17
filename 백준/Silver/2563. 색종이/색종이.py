import sys
list = [[0]*100 for _ in range(100)]
area = 0
for _ in range(int(input())):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(10):
        for j in range(10):
            list[x+i][y+j] = 1
for i in range(100):
    area += list[i].count(1)
print(area)