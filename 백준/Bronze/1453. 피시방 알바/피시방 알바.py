n = int(input())
arr = list(map(int, input().split()))
seat = [0]*100
cnt = 0
for i in arr:
    if seat[i-1] == 0:
        seat[i-1] = 1
    else:
        cnt += 1
print(cnt)