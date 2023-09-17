def failure(pattern):
    length = len(pattern)
    table = [0 for _ in range(length)]
    j = 0
    for i in range(1, length):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return max(table)

s = input()
result = 0

for idx in range(len(s)):
    sub_str = s[idx:len(s)]
    result = max(result, failure(sub_str))

print(result)