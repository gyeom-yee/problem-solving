def solution(s, skip, index):
    answer = []
    alpha_li = [c for c in "abcdefghijklmnopqrstuvwxyz" if c not in skip]
    for c in s:
        temp_idx = alpha_li.index(c)
        answer.append(alpha_li[(temp_idx+index)%len(alpha_li)])
    return "".join(answer)