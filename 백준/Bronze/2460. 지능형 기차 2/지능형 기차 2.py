humans = 0
res = 0
for _ in range(10):
    down, up = map(int, input().split())
    humans -= down
    humans += up
    if res < humans:
        res = humans
print(res)