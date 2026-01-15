def solution(n):
    prime_li = [True]*(n+1)
    for i in range(2, int(n**0.5)+1):
        if prime_li[i]:
            for j in range(i*i, n+1, i):
                prime_li[j] = False
    return sum(prime_li[2:])