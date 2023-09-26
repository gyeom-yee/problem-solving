import sys
n = int(sys.stdin.readline())
st = sys.stdin.readline().split()
qs = sys.stdin.readline().split()
m = int(sys.stdin.readline())
x_arr = sys.stdin.readline().split()
ans = []
q = [qs[i] for i in range(n) if st[i] == "0"]
q.reverse()
print(" ".join((q+x_arr)[:m]))