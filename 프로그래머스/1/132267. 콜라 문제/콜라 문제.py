def solution(a, b, n):
    answer = 0
    while n >= a:
        temp = n%a
        cola = n//a * b
        answer += cola
        n = cola + temp
    return answer