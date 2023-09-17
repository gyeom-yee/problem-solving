import sys
gomgom = {}
cnt = 0
for i in range(int(input())):
    name = sys.stdin.readline().rstrip()
    if name == "ENTER":
        gomgom.clear()
        continue
    if name in gomgom:
        continue
    else:
        cnt += 1
        gomgom[name] = 1
print(cnt)