import sys

def permutation_repetition(arr, m):
    for i in range(len(arr)):
        if m == 1:
            yield arr[i]
        else:
            for next in permutation_repetition(arr, m-1):
                yield arr[i] + " " + next
n, m = map(int, sys.stdin.readline().split())
pr = permutation_repetition(list(map(str, range(1, n+1))), m)
sys.stdout.write("\n".join(pr))