def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        temp = format(arr1[i] | arr2[i], f"0{n}b")
        answer.append(temp.replace("1", "#").replace("0", " "))
    return answer

