def combination(arr, r):
    arr = sorted(arr)

    def generate(chosen):
        global max, m
        if len(chosen) == r:
            if max < sum(chosen) <= m:
                max = sum(chosen)
            return

        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for next in range(start, len(arr)):
            chosen.append(arr[next])
            generate(chosen)
            chosen.pop()
    generate([])

n, m = map(int, input().split())
n_li = list(map(int, input().split()))
max = 0
combination(n_li, 3)
print(max)