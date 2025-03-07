dice = ['E', 'A', 'B', 'C', 'D']
for _ in range(3):
    stick = list(map(int, input().split()))
    cnt_zero = 0
    for i in stick:
        if i == 0: cnt_zero += 1
    print(dice[cnt_zero])