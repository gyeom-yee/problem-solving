import sys
n_li = []
for _ in range(int(input())):
    n_li.append(int(sys.stdin.readline()))
print(*sorted(n_li), sep='\n')