a, b = map(int, input().split())
c, d = map(int, input().split())

bottom = b*d
top = a*d + c*b
x, y = top, bottom

while bottom:
    top, bottom = bottom, top%bottom

print(x//top, y//top)