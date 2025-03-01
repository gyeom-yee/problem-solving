E, S, M = map(int, input().split())
n_e, n_s, n_m = 0, 0, 0
result = 0
while True:
    if n_e == E and n_s == S and n_m == M:
        break
    n_e += 1
    n_s += 1
    n_m += 1
    if n_e%16 == 0:
        n_e = 1
    if n_s%29 == 0:
        n_s = 1
    if n_m%20 == 0:
        n_m = 1
    result += 1
print(result)