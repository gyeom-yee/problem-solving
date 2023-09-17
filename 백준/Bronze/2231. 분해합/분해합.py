n = int(input())
for i in range(n-len(str(n))*9, n+1):
    new = 0
    n_i = i
    if i <= 0: continue
    else:
        while 1:
            new += n_i%10
            if not n_i//10: break
            n_i //= 10
        if i+new == n:
            print(i)
            break
        elif i >= n:
            print(0)
            break