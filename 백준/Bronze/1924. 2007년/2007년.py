x, y = map(int, input().split())
month_li = []
day_li = []
week_li = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

for m in range(1, x+1):
    for d in range(1, 32):
        day_li.append(d)
        if len(day_li) == 7:
            month_li.append(day_li)
            day_li = []
        if m == x and d == y: break
        elif d == 28 and m == 2: break
        elif d == 30 and m in [4, 6, 9 ,11]: break
month_li.append(day_li)
print(week_li[len(month_li[-1])-1])