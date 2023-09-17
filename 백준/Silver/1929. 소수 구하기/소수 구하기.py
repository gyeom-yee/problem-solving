m, n = map(int, input().split())
p_list = [1]*(n+1)
p_list[1] = 0
for i in range(2, int(n**0.5)+1):
    if p_list[i]:
        for j in range(i*i, n+1, i):
            p_list[j] = 0
print("\n".join([f"{i}" for i in range(m, n+1) if p_list[i] == 1]))