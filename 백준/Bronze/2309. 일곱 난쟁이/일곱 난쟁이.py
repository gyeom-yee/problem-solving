from itertools import combinations

arr = sorted([int(input()) for _ in range(9)])
for combo in combinations(arr, 7):
    if sum(combo) == 100:
        print("\n".join(map(str, combo)))
        break