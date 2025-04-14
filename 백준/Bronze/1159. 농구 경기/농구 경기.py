import sys
input = sys.stdin.readline
n = int(input())
name_dict = dict()
flag = 0
arr = []

for _ in range(n):
    first_name = input()
    if first_name[0] not in name_dict:
        name_dict[first_name[0]] = 1
    else:
        name_dict[first_name[0]] += 1
for key, val in name_dict.items():
    if val >= 5:
        flag = 1
        arr.append(key)
arr.sort()
print("".join(arr) if flag else "PREDAJA")