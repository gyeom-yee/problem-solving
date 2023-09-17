def substring(s, l):
    subs = set()
    for i in range(len(s)-(l-1)):
        subs.add(s[i:i+l])
    return subs

word = input()
substrs=0
for i in range(len(word)):
    substrs+=len(substring(word, i+1))
print(substrs)