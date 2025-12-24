def solution(arr, divisor):
    answer = sorted([a for a in arr if a%divisor == 0])
    return answer if answer else [-1]