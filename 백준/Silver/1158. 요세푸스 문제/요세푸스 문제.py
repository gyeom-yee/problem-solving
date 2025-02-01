n, k = map(int, input().split())
n_li = [i for i in range(1, n+1)]
result = []
j = -1
for _ in range(n) :
    j += k
    if j >= len(n_li):
        j %= len(n_li)
    result.append(n_li.pop(j))
    j -= 1
print('<', end='')
print(*result, sep=', ', end='')
print('>')