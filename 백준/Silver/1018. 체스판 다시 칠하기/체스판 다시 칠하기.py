def chess(x, y):
    w_st = 0
    b_st = 0
    for k in range(x, x+8):
        for l in range(y, y+8):
            if (k+l)%2 == 0:
                if c[k][l] != 'W': w_st += 1
                if c[k][l] != 'B': b_st += 1
            else:
                if c[k][l] != 'W': b_st += 1
                if c[k][l] != 'B': w_st += 1
    return w_st, b_st

n, m, *c = open(0).read().split(); n, m = int(n), int(m)
result = []
for i in range(n-7):
    for j in range(m-7):
        result.extend(chess(i, j))
print(min(result))