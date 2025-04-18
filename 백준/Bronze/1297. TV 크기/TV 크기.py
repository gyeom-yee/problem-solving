from math import sqrt
D, H, W = map(int, input().split())
n = D/sqrt(H**2 + W**2)
print(int(n*H), int(n*W))