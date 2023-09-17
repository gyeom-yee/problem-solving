n = int(input())
result = 1
gap = 0
while True:
    result += 6 * gap
    if result >= n: break
    gap += 1
print(gap+1)