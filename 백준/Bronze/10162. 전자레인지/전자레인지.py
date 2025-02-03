T = int(input())

if T % 10 != 0:
    print(-1)
else:
    btn = [0] * 3
    btn_n = [300, 60, 10]

    for i in range(3):
        btn[i] = T // btn_n[i]
        T %= btn_n[i]
    print(*btn)