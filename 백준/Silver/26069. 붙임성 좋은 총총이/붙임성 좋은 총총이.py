import sys
dance = set(["ChongChong"])
meet = sys.stdin.readlines()[1:]
for x in meet:
    a, b = x.split()
    if a in dance:
        if b in dance: continue
        else: dance.add(b)
    elif b in dance:
        if a in dance: continue
        else: dance.add(a)
print(len(dance))