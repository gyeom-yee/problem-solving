def exam(n, m):
    def permutation(idx, depth):
        if depth == m:
            print(" ".join(choices))
            return

        for i in range(1, n+1):
            if str(i) in choices:
                continue
            choices.append(str(i))
            permutation(i, depth+1)
            choices.pop()
    permutation(1,0)

choices = []
n, m = map(int, input().split())
exam(n,m)