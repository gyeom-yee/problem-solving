star_n = int(input())
for i in range(star_n, 0, -1):
    print(" "*(star_n-i), "*"*i, sep="")