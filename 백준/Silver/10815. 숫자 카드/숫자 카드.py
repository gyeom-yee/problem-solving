import sys
n = sys.stdin.readline()
card = set(sys.stdin.readline().split())
m = sys.stdin.readline()
bool_card = sys.stdin.readline().split()
print("".join("1 " if i in card else "0 " for i in bool_card))