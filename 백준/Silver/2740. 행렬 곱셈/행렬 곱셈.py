n, m = map(int, input().split())
matrix_a = [list(map(int, input().split())) for _ in range(n)]

_, k = map(int, input().split())
matrix_b = [list(map(int, input().split())) for _ in range(m)]

result = []
for i in range(n):
    rows = []
    for j in range(m):
        tmp = []
        for x in range(k):
            tmp.append(matrix_a[i][j]*matrix_b[j][x])
        rows.append(tmp)
    result.append([sum(col) for col in zip(*rows)])
for i in range(n):
    for j in range(k):
        print(result[i][j], end=" ")
    print()