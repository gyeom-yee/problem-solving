import sys
member_list = [list() for _ in range(201)]
for _ in range(int(input())):
    age, name = sys.stdin.readline().split()
    member_list[int(age)].append(name)
for m in range(len(member_list)):
    if len(member_list[m]) == 0:
        continue
    else: 
        for i in member_list[m]:
            print(m, i)