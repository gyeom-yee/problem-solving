import sys
def combination_repetition(arr, m):
    for i in range(len(arr)):
        if m == 1:
            yield arr[i]
        else:
            for next in combination_repetition(arr[i:], m-1):
                yield arr[i] + " " + next
n, m = map(int, sys.stdin.readline().split())
cr = combination_repetition(list(map(str, range(1, n+1))), m)
sys.stdout.write("\n".join(cr))