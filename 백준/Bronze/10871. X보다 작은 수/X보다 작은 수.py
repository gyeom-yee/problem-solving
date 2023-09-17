n, x = map(int, input().split())
a = list(map(int, input().split()))
a = [value for value in a if value < x]
print(*a)