n = int(input())
for i in range(n):
    print('*' + (' '+'*')*(n//2-(n%2==0)))
    print((' ' + '*') * (n//2))