import sys
input = sys.stdin.readline

n = input()
h = len(n)
n = int(n)
result = 0

for i in range(n-h*9, n):
    tmp = i
    tmp_sum = 0
    if i <= 0: continue
    else:
        while tmp//10 != 0:
            tmp_sum += tmp%10
            tmp //= 10
        if i+tmp+tmp_sum == n:
            result = i
            break

print(result)