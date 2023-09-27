import sys
dance = set(["ChongChong"])
meet = sys.stdin.readlines()[1:]
for x in meet:
    a, b = x.split()
    if a in dance:
        dance.add(b)
    elif b in dance:
        dance.add(a)
print(len(dance))
