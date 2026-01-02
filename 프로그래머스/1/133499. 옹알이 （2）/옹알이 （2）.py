def solution(babbling):
    answer = 0
    for word in babbling:
        for c in ["aya", "ye", "woo", "ma"]:
            if c*2 not in word:
                word = word.replace(c, " ")
        if not word.strip(): answer += 1
    return answer