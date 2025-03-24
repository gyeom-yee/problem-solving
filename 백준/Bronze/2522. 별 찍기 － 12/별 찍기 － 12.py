n = int(input())
for i in range(-n+1, n):
    print(' '*i+'*'*(n-i) if i > 0 else ' '*abs(i)+'*'*(n+i))