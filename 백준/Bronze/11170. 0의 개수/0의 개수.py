t = int(input())
for _ in range(t):
    start, end = map(int, input().split())
    print("".join(map(str, range(start, end+1))).count('0'))