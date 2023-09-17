s = sorted(list(map(int, input().split())))
if s[0] == s[1] == s[2]:
    print(sum(s))
elif s[2] >= s[0]+s[1]:
    s[2] = s[0]+s[1]-1
    print(sum(s))
else: print(sum(s))