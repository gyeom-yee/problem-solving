def solution(num):
    answer = 0
    
    if num == 1:
        pass
    else:
        for i in range(1, 501):
            if num%2 == 0: 
                num //= 2
                if num == 1: break
            else:
                num = num*3 + 1
        answer = (i if num==1 else -1)
    return answer