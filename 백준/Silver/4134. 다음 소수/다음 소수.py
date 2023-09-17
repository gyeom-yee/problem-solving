def isPrime(x):
    if x < 2: return 0
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0: return 0
    else: return 1

import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    while isPrime(n) == 0:
        n += 1
    print(n)