def solution(x):
    result = 0
    for c in str(x):
        result += int(c)
    return True if x%result == 0 else False