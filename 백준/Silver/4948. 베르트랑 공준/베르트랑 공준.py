import sys
def prime(x):
    l = [1] * (2 * x + 1)
    l[0] = 0

    for i in range(2, int(2 * x ** 0.5) + 1):
        if l[i]:
            for j in range(i * i, 2 * x + 1, i):
                l[j] = 0
    return l

primeList = prime(123456)

while 1:
    n = int(sys.stdin.readline())
    if n == 0: break
    else: print(sum(primeList[n+1:2*n+1]))