def solution(numbers):
    from itertools import combinations
    answer = set()
    for c in combinations(numbers, 2):
        answer.add(sum(c))
    answer = sorted(answer)
    return answer