from math import prod
N = input()
flag = 'NO'
for i in range(1, len(N)):
    if prod(list(map(int, N[:-i]))) == prod(list(map(int, N[-i:]))):
        flag = 'YES'
        break
print(flag)