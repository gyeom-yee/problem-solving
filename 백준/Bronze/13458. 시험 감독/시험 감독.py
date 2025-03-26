import math
n = int(input())
a_li  = list(map(int, input().split()))
b, c = map(int, input().split())
cnt = n

for cls in a_li:
    cls -= b
    if cls > 0:
        cnt += math.ceil(cls / c)
print(cnt)