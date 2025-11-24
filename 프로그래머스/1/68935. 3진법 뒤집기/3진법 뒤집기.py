def solution(n):
    answer = 0
    temp = ""
    while n//3:
        temp = str(n%3) + temp
        n //= 3
    temp = str(n) + temp
    for i in range(len(temp)):
        answer += (3**i)*int(temp[i])
    return answer