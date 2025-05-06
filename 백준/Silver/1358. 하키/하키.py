import sys
input = sys.stdin.readline

W, H, X, Y, P = map(int, input().split())
cnt = 0

def is_inside_circle(x, y, cx, cy):
    return (x - cx)**2 + (y - cy)**2 <= (H/2)**2

for _ in range(P):
    dx, dy = map(int, input().split())
    if X <= dx <= X+W and Y <= dy <= Y+H:
        cnt += 1
    elif is_inside_circle(dx, dy, X, Y+(H/2)) or is_inside_circle(dx, dy, X+W, Y+H/2):
        cnt += 1
print(cnt)