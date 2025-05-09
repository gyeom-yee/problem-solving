from itertools import combinations
a, b = map(int, input().split())
arr = list(range(1, 11))*2
arr.remove(a)
arr.remove(b)
rank = list(combinations(arr, 2))
rank.sort(key=lambda x: (x[0] == x[1], (x[0]+x[1])%10 if x[0] != x[1] else x[0]))
if a == b:
    print(f'{1-((10-a)/len(rank)):.3f}')
else:
    for i, tup in enumerate(rank):
        if sum(tup)%10 >= (a+b)%10:
            print(f'{i/len(rank):.3f}')
            break