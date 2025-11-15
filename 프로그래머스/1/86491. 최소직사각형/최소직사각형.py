def solution(sizes):
    answer = 0
    temp = [sorted(x) for x in sizes]
    answer = max(temp, key=lambda x : x[0])[0] * max(temp, key=lambda x : x[1])[1]
    return answer