n = int(input())
arr = list(map(int, input().split()))
prime_cnt = n
for i in arr:
    if i == 1: prime_cnt -= 1
    else:
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                prime_cnt -= 1
                break
print(prime_cnt)