n, m = map(int, input().split())
dna_li = [input() for _ in range(n)]
res = ''
hd = 0

for i in range(m):
    cnt = {'A':0, 'C':0, 'G':0, 'T':0}
    for j in range(n):
        cnt[dna_li[j][i]] += 1
    max_char = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))[0][0]
    res += max_char
    hd += sum(1 for j in range(n) if dna_li[j][i] != max_char)
print(res, hd, sep='\n')