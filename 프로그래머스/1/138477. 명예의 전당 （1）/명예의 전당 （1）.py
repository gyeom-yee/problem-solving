def solution(k, score):
    answer = []
    honor = []
    
    for i in range(len(score)):
        honor.append(score[i])
        honor.sort()
        if i < k:
            answer.append(honor[0])
        else:
            answer.append(honor[-k])
    return answer