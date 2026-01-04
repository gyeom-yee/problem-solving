def solution(answers):
    user = {1:0, 2:0, 3:0}
    first = [1,2,3,4,5]*2000
    second= [2,1,2,3,2,4,2,5]*1250
    third = [3,3,1,1,2,2,4,4,5,5]*1000
    
    for i in range(len(answers)):
        if answers[i] == first[i]: user[1] += 1
        if answers[i] == second[i]: user[2] += 1
        if answers[i] == third[i]: user[3] += 1
    max_score = max(user.items(), key=lambda x:x[1])[1]

    return [x[0] for x in sorted(user.items(), key=lambda x:x[1], reverse=True) if x[1] >= max_score]