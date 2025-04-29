import sys
input = sys.stdin.readline

N = int(input())
arr = sorted([int(input()) for _ in range(N)], reverse=True)
result_arr = [arr[i-1] for i in range(1, N+1) if i%3 != 0]
print(sum(result_arr))
