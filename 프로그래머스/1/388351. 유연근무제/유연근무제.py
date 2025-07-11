def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        flag = 1
        tempday = startday
        end = 0
        if schedules[i] % 100 >= 50:
            end = (schedules[i] % 10) + (schedules[i] // 100 * 100) + 100
        else:
            end = schedules[i] + 10

        for j in range(len(timelogs[i])):
            if timelogs[i][j] > end and (tempday not in [6, 7]):
                flag = 0
            tempday = (tempday % 7) + 1
        if flag:
            answer += 1
    return answer