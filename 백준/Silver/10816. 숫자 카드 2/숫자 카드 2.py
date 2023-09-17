import sys
card, cnt_card = sys.stdin.read().split("\n")[1::2]
card = card.split()
cnt_card = cnt_card.split()
dict_card = dict()
res = []
for i in card:
    if i in dict_card:
        dict_card[i] += 1
    else:
        dict_card[i] = 1
for j in cnt_card:
    res.append(dict_card.get(j, 0))
sys.stdout.write(' '.join(str(r) if r else '0' for r in res))