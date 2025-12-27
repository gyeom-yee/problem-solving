def solution(arr):
    temp = ""
    answer = []
    for a in arr:
        if temp != a:
            temp = a
            answer.append(a)
    return answer