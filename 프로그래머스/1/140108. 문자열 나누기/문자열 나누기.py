def solution(s):
    first = s[0]
    first_cnt = 1
    other_cnt = 0
    cnt = 1
    for c in s[1:]:
        if first_cnt == other_cnt:
            cnt += 1
            first = c
            first_cnt, other_cnt = 1, 0
            continue

        if first == c: first_cnt += 1
        else: other_cnt += 1
    return cnt