def solution(name, yearning, photo):
    answer = []
    name_dict = {name[i]:yearning[i] for i in range(len(name))}
    for p in photo:
        temp = 0
        for human in p:
            if human not in name_dict: continue
            temp += name_dict[human]
        answer.append(temp)
    return answer