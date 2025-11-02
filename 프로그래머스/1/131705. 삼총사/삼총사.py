from itertools import combinations

def solution(number):
    answer = 0
    
    for ns in combinations(number, 3):
        if sum(ns) == 0:
            answer += 1
    return answer