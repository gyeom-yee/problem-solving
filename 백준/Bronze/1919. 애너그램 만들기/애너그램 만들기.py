word1 = input()
word2 = input()
word1_cnt = [0]*26
word2_cnt = [0]*26
cnt = 0
for i in word1:
    word1_cnt[ord(i)-ord('a')] += 1
for j in word2:
    word2_cnt[ord(j)-ord('a')] += 1
for k in range(26):
    if word1_cnt[k] and word2_cnt[k]:
        cnt += min(word1_cnt[k], word2_cnt[k])
print(len(word1)+len(word2)-cnt*2)