n = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

minnum, maxnum = 1e10, -1e10

def dfs(i, ans, add, sub, mul, div):
    global minnum, maxnum
    if i == n:
        maxnum = max(maxnum, ans)
        minnum = min(minnum, ans)
        return

    else:
        if add:
            dfs(i+1, ans+arr[i], add-1, sub, mul, div)
        if sub:
            dfs(i+1, ans-arr[i], add, sub-1, mul, div)
        if mul:
            dfs(i+1, ans*arr[i], add, sub, mul-1, div)
        if div:
            if ans < 0:
                dfs(i+1, -(-ans//arr[i]), add, sub, mul, div-1)
            else:
                dfs(i+1, ans//arr[i], add, sub, mul, div-1)

dfs(1, arr[0], add, sub, mul, div)
print(maxnum, minnum, sep='\n')