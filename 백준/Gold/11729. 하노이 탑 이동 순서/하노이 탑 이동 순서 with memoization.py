import sys
def hanoi(n, from_pos, by_pos, to_pos):
    key = (n, from_pos, by_pos, to_pos)
    if key in memo:
        return memo[key]
    elif n == 1:
        return f"{from_pos} {to_pos}"
    tmp = "\n".join([hanoi(n-1, from_pos, to_pos, by_pos), f"{from_pos} {to_pos}", hanoi(n-1, by_pos, from_pos, to_pos)])
    memo[key] = tmp
    return tmp

ans = []
memo = dict()
n = int(sys.stdin.readline())
print(2**n -1)
sys.stdout.write(hanoi(n, 1, 2, 3))
