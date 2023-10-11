def dfs(x):
    global ans
    if x == n:
        ans += 1
        return
    else:
        for i in range(n):
            row[x] = i
            if isPossible(x):
                dfs(x+1)

def isPossible(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x-i:
            return False
    return True
n = int(input())
row = [0]*n
ans = 0
dfs(0)
print(ans)