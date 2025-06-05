s = 0
n_dict = {}
for _ in range(10):
    tmp = int(input())
    s += tmp
    if tmp in n_dict:
        n_dict[tmp] += 1
    else:
        n_dict[tmp] = 0
print(s//10)
print(max(n_dict, key=n_dict.get))