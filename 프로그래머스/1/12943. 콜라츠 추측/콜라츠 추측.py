def solution(num):
    answer = 0
    cnt = 0
    
    if num == 1:
        pass
    else:
        while num != 1 and cnt < 500:
            cnt += 1
            if num%2 == 0: 
                num //= 2
            else:
                num = num*3 + 1
        answer = (cnt if num==1 else -1)
    return answer