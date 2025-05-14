import sys
input = sys.stdin.readline

prime = [True for _ in range(1_000_000+1)]
for i in range(2, int((1_000_000**(1/2)))+1):
    if prime[i] == True:
        j=2
        while i*j<1_000_000:
            prime[i*j]=False
            j += 1

for _ in range(int(input())):
    s = int(input())
    for i in range(2, len(prime)):
        if prime[i] == True and s%i == 0:
            print('NO')
            break
    else: print('YES')