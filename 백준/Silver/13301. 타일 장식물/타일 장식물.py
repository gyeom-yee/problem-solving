n = int(input())
arr = [0, 1]
res = 4
if n == 1:
    pass
else:
    for i in range(2, n+1):
        now = arr[i-2]+arr[i-1]
        arr.append(now)
        res += now*2
print(res)