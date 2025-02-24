n, m = map(int, input().split())
n_li = sorted(list(map(int, input().split())))
used = [0]*n

def perm(arr, r):
    if r == m:
        print(*arr)
        return
    for i in range(n):
        if not used[i]:
            used[i] = 1
            arr.append(n_li[i])
            perm(arr, r+1)
            arr.pop()
            used[i] = 0
perm([], 0)