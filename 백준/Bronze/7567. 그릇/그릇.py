plates = input()
result = 10
for i in range(1, len(plates)):
    if plates[i-1] == plates[i]:
        result += 5
    else:
        result += 10
print(result)