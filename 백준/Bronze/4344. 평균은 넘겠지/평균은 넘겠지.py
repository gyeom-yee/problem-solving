import sys
for _ in range(int(input())):
    count = 0
    score_list = list(map(int, sys.stdin.readline().split()))
    n = score_list.pop(0)
    avg = sum(score_list)/n
    for i in score_list:
        if i > avg:
            count += 1
    print("%.3f%%" %(count/n*100))