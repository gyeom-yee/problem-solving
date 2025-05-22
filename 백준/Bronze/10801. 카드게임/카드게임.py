a_li = list(map(int, input().split()))
b_li = list(map(int, input().split()))

a_score = 0
b_score = 0
for a, b in zip(a_li, b_li):
    if a > b: a_score += 1
    elif a < b: b_score += 1
if a_score > b_score: print('A')
elif a_score < b_score: print('B')
else: print('D')