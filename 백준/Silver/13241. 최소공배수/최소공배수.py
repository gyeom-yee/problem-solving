a, b = map(int, input().split())
x, y = a, b

while b:
    a, b = b, a%b

print(x*y//a)