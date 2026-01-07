def solution(dartResult):
    import re
    result = re.findall(r'(\d+)([SDT])([*#]?)', dartResult)
    bonus_dict = {'S':1, 'D':2, 'T':3}
    option_dict = {'':1, '*':2, '#':-1}
    scores = []
    
    for s, b, o in result:
        temp = (int(s) ** bonus_dict[b]) * option_dict[o]
        if o == '*' and scores: scores[-1] *= 2
        scores.append(temp)
    return sum(scores)