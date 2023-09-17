n = int(input())
arr = list(map(int, input().split()))
max_score = max(arr)
sum_score = 0
for i in arr:
    sum_score += i/max_score*100
print(sum_score/n)