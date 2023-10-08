import sys
def combination(arr, m):
    for i in range(len(arr)):
        if m == 1:
            yield [arr[i]]
        else:
            for next in combination(arr[i+1:], m-1):
                yield [arr[i]] + next
n, m = map(int, input().split())
c = combination(list(map(str, range(1, n+1))), m)
sys.stdout.write("\n".join(map(" ".join, c)))