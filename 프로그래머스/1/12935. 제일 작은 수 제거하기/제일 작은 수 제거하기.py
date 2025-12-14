def solution(arr):
    answer = []
    idx = arr.index(min(arr))
    arr.pop(idx)
    return arr if arr else [-1]