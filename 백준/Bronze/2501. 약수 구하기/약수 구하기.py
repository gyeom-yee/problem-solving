n, k = map(int, input().split())
arr = []
for i in range(1,n+1):
    if n%i == 0:
        arr.append(i)
print(0 if len(arr)-1 < k-1 else arr[k-1])