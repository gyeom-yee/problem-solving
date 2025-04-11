import sys
input = sys.stdin.readline
n = int(input())
t = [i*(i+1)//2 for i in range(1, 46)]
result = [0]*1001
for i in t:
    for j in t:
        for k in t:
            if i+j+k <= 1000:
                result[i+j+k] = 1
for _ in range(n):
    print(result[int(input())])