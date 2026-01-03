def solution(N, stages):
    total = len(stages)
    s_dict = {i:0 for i in range(1, N + 2)}
    fail_dict = {}
    
    for s in stages:
        s_dict[s] += 1
    
    for k, v in s_dict.items():
        if k > N: break
        if total == 0: total = 1e-9
        fail_dict[k] = v/total
        total -= v

    answer = [x[0] for x in sorted(fail_dict.items(), key=lambda x : x[1], reverse=True)]
    return answer