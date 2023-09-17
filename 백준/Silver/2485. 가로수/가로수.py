def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

n, *a = open(0).read().split()
a = list(map(int, a))
a_ = [a[i]-a[i-1] for i in range(1, len(a))]
gcd_all = a_[0]
for i in range(1, len(a_)):
    gcd_all = gcd(gcd_all, a_[i])
print((a[-1] - a[0])//gcd_all-(len(a)-1))