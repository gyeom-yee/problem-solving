import sys
input = sys.stdin.readline
d = dict()
n, m = map(int, input().split())
for _ in range(n):
    word = input().rstrip()
    if len(word) >= m:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
d = sorted(d.items())
d = sorted(d, key=lambda item:len(item[0]), reverse=True)
d = dict(sorted(d, key=lambda item:item[1], reverse=True))
sys.stdout.write("\n".join(d))