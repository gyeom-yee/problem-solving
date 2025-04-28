import sys
input = sys.stdin.readline

L = int(input())
N = int(input())
cake = [0]*L
result_max = 0
result_max_idx = 0
result_real = 0
result_real_idx = 0

for i in range(1, N+1):
    P, K = map(int, input().split())
    if K-P > result_max:
        result_max = K-P
        result_max_idx = i
    cnt = 0
    for j in range(P,K+1):
        if cake[j-1] == 0:
            cake[j-1] = i
            cnt += 1
    if cnt > result_real:
        result_real = cnt
        result_real_idx = i
print(result_max_idx, result_real_idx, sep='\n')