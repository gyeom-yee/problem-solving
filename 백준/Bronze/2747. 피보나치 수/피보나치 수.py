n = int(input())
fibo = [0,1,1] + [0]*(n-2)

for i in range(3, n+1):
    fibo[i] = fibo[i-1] + fibo[i-2]
print(fibo[n])