def solution(numbers):
    no_numbers = [n for n in range(10) if n not in numbers]
    return sum(no_numbers)