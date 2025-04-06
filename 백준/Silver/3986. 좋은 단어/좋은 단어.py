import sys
input = sys.stdin.readline

n = int(input())
result = 0
for _ in range(n):
    s = input().rstrip()
    if len(s) % 2 != 0: continue
    if s == s[::-1]: result += 1
    else:
        while 'AA' in s or 'BB' in s:
            if 'AA' in s: s = s.replace('AA', '')
            else: s = s.replace('BB', '')
        if not s:
            result += 1
print(result)