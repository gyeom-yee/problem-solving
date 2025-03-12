n = int(input())
dp = [1, 3]+[0]*999
for i in range(2, n):
    dp[i] = dp[i-1] + 2*dp[i-2]
print(dp[n-1]%10007)