import sys
input = sys.stdin.readline
input()
n_arr = set(input().split())
input()
m_arr = input().split()
sys.stdout.write("\n".join(["1" if x in n_arr else "0" for x in m_arr]))
