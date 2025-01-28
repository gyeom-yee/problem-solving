n = int(input())
fibo_li = [0, 1, 1] + [0]*(n-2)
for i in range(3, n+1):
    fibo_li[i] = fibo_li[i-2] + fibo_li[i-1]
print(fibo_li[-1])