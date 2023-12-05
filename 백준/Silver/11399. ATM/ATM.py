input()
p_list = [0]+sorted(list(map(int, input().split())))
sum_li = [0]*(len(p_list))

for i in range(1, len(sum_li)):
    sum_li[i] = sum_li[i-1] + p_list[i]
print(sum(sum_li))