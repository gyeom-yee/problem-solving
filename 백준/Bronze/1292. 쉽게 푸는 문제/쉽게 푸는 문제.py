a, b = map(int, input().split())
arr = [0]*1000
i = 1
idx = 0
while arr[-1] == 0:
    for _ in range(i):
        arr[idx] = i
        idx += 1
        if arr[-1] != 0: break
    i += 1
print(sum(arr[a-1:b]))