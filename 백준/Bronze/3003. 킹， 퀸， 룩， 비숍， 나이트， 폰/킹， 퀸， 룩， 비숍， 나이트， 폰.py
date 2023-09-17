pin = [1,1,2,2,2,8]
find_pin = list(map(int, input().split()))
for i in range(len(pin)):
    print(pin[i]-find_pin[i], end=" ")