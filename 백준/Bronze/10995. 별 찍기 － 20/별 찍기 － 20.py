n = int(input())
for i in range(1, n+1):
    print((' *' if i%2==0 else '*') + (' *' * (n - 1)))
