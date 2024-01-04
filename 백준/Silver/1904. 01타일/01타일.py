import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (1000000 + 1)
dp[1] = 1 # 1번째의 결과값
dp[2] = 2 # 2번째의 결과값
dp[3] = 3

for index in range(3, 1000000 + 1): # (가장 처음 점화식으로 계산되는 번째, 최대치 + 1)
    dp[index] = (dp[index - 1] + dp[index - 2]) % 15746 # 점화식
print (dp[n]) # N 번째 값 출력