s = input()
flag = 2
dasom = {'0':0, '1':0}
for i in s:
    if i != flag:
        dasom[i] += 1
        flag = i
print(min(dasom.values()))