n = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_sum, max_sum = 1e10, -1e10

def dfs(i, ans, add, sub, mul, div):
    global min_sum, max_sum
    if i == n:
        max_sum = max(max_sum, ans)
        min_sum = min(min_sum, ans)
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
print(max_sum, min_sum, sep='\n')