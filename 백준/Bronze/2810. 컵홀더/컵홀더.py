N = int(input())
humans = input()
humans = humans.replace('S', '*S').replace('LL', '*LL')
print(min(N, humans.count('*')+1))