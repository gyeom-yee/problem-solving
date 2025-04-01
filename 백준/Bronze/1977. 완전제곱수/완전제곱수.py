m = int(input())
n = int(input())
arr = [i*i for i in range(1, 101) if m <= i*i <= n]
if arr:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)