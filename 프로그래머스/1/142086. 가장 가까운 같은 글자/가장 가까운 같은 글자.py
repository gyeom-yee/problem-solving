def solution(s):
    answer = []

    alpha_list = [None] * 26

    for i in range(len(s)):
        a = ord(s[i]) - 97
        if alpha_list[a] is None:
            alpha_list[a] = i
            answer.append(-1)
        else:
            answer.append(i - alpha_list[a])
            alpha_list[a] = i
    return answer