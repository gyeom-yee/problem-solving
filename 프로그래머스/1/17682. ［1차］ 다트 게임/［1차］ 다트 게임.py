def solution(dartResult):
    import re
    result = re.findall(r'(\d+)([SDT])([*#]?)', dartResult)
    bonus_dict = {'S':1, 'D':2, 'T':3}
    scores = []
    
    for s, b, o in result:
        temp = int(s) ** bonus_dict[b]
        
        if o == '*':
            temp *= 2
            if scores:
                scores[-1] *= 2
        elif o == '#':
            temp *= -1
        scores.append(temp)
    return sum(scores)