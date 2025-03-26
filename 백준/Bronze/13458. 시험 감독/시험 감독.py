import math
n = int(input())
a_li  = list(map(int, input().split()))
b, c = map(int, input().split())
result = []

for cls in a_li:
    cnt = 0
    if cls > b:
        cls -= b
        if cls > c:
            cnt = math.ceil(cls / c) + 1
        else:
            cnt += 2
    else:
        cnt += 1
    result.append(cnt)
print(sum(result))