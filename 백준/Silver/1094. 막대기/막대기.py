x = int(input())
stick = 64
short = stick/2
cnt = 1
while stick > x:
    if stick-short >= x:
        stick -= short
        short /= 2
        cnt -= 1
    else:
        short /= 2
    cnt += 1
print(cnt)