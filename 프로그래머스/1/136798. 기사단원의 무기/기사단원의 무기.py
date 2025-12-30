def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        temp = 0
        for a in range(1, int(i**0.5)+1):
            if a*a == i:
                temp += 1
            elif i%a == 0:
                temp += 2
        answer += power if temp > limit else temp
    return answer