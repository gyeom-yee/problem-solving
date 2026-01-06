def solution(nums):
    from itertools import combinations
    answer = 0
    
    for x in combinations(nums, 3):
        temp = sum(x)
        flag = True
        for i in range(2, int(temp**0.5)+1):
            if temp%i == 0:
                flag = False
                break
        answer += 1 if flag else 0
    return answer