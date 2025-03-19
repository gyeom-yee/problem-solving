a, b, c = map(int, input().split())
d = int(input())
total = a*3600+b*60+c+d
new_a = total//3600%24
total %= 3600
new_b = total//60
new_c = total%60
print(new_a, new_b,  new_c)
