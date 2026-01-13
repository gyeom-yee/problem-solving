def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt = 0
    zero_cnt = 0
    for n in lottos:
        if n in win_nums: cnt += 1
        elif n == 0: zero_cnt += 1
    return [rank[cnt+zero_cnt], rank[cnt]]