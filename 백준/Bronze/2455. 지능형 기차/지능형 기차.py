top = -1
train = 0
for _ in range(4):
    a, b = map(int, input().split())
    train += b-a
    if train > top:
        top = train
print(top)