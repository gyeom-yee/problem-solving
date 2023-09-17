import sys
def prime(x):
    eratos = [0,0] + [1] * (x+1)
    for i in range(2, int(x**0.5)+1):
        if eratos[i]:
            for j in range(i*i,x+1, i):
                eratos[j] = 0
    prime = [idx for idx,v in enumerate(eratos) if v]
    return eratos, prime

eratos, p_list = prime(1000000)
for _ in range(int(input())):
    n = int(sys.stdin.readline())
    cnt = 0
    for x in p_list:
        tmp = n-x
        if tmp < x: break
        else:
            if eratos[tmp]:
                cnt += 1
    print(cnt)