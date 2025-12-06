def gcd(x, y):
    if x%y == 0:
        return y
    else:
        return gcd(y, x%y)

def lcm(x, y):
    return x*y/gcd(x, y)

def solution(n, m):
    answer = [gcd(n,m), lcm(n,m)]
    return answer