import sys
input = sys.stdin.readline
input()
n_arr = {x for x in input().split()}
input()
m_arr = input().split()
ans = []
for x in m_arr:
    ans.append("1" if x in n_arr else "0")
sys.stdout.write("\n".join(ans))