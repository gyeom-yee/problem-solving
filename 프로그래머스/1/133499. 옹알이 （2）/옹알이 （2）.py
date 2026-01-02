def solution(babbling):
    answer = 0
    for word in babbling:
        word = word.replace("aya", "1").replace("ye", "2").replace("woo", "3").replace("ma", "4")
        if word.isdigit():
            for i in range(1, len(word)):
                if word[i-1] == word[i]:
                    break
            else: answer += 1
        else: pass
    return answer