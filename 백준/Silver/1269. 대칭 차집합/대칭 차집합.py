import sys
A, B = sys.stdin.read().split("\n")[1:3]
print(len({*A.split()}^{*B.split()}))