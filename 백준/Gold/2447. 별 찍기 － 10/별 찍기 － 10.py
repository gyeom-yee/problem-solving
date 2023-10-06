def star_stamp(n):
    if n == 1:
        return ["*"]
    stars = star_stamp(n//3)
    ans = []
    for x in stars:
        ans.append(x*3)
    for x in stars:
        ans.append(x + " "*(n//3) + x)
    for x in stars:
        ans.append(x*3)
    return ans

n = int(input())
print("\n".join(star_stamp(n)))
