import sys
input = sys.stdin.readline
n = int(input())
arr = []
d = dict()
ans = []

def roundTraditional(val, digits):
    return int(round(val+10**(-len(str(val))-1), digits))

for _ in range(n):
    x = int(input())
    arr.append(x)
    if x in d: d[x]+=1
    else: d[x]=1
arr.sort()
ans.append(str(roundTraditional(sum(arr)/n, 0)))
ans.append(str(arr[n//2]))
d = sorted(d.items(), key=lambda item: item[1], reverse=True)
many = []
for i in range(len(d)):
    if d[0][1] == d[i][1]:
        many.append(d[i][0])
many.sort()
ans.append(str(many[1] if len(many) > 1 else many[0]))
ans.append(str(arr[-1]-arr[0]))
sys.stdout.write("\n".join(ans))