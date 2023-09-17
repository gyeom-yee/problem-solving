s = input().upper()
max_idx = 0
for i in range(26):
    cnt = s.count(chr(i+65))
    if max_idx < cnt:
        max_idx = cnt
        max_char = chr(i+65)
    elif max_idx == cnt:
        max_char = '?'
print(max_char)