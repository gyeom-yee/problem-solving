t = int(input())
arr = list(map(str, range(0, 1_000_001)))
zero = [0]*1_000_001
for i in range(1_000_001):
    zero[i] = arr[i].count('0')
for _ in range(t):
    start, end = map(int, input().split())
    print(sum(zero[start:end+1]))