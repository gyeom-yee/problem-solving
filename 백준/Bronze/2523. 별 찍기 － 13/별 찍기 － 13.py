n = int(input())
for i in range(-n+1, n):
    if i >= 0:
        print('*'* (n-i))
    else:
        print('*' * (abs(i+n)))