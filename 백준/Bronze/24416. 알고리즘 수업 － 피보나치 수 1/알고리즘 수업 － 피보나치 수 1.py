# def fibonacci(n):
#     global fib1_call
#     if n==1 or n==2:
#         fib1_call += 1
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

def fibonacci2(n):
    global fib2_call
    for i in range(2, n):
        fib[i] = fib[i-2]+fib[i-1]
        fib2_call += 1
    return fib[n-1]

n = int(input())
# fib1_call = 0
fib2_call = 0
fib = [1, 1] + [0] * (n - 1)
# fibonacci(n)
fibonacci2(n)
fib1_call = ((1+(5**(1/2)))**n - (1-(5**(1/2)))**n) / ((2**n) * (5**(1/2)))
print(int(fib1_call), fib2_call)