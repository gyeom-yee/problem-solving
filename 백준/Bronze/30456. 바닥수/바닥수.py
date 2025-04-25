N, L = map(int, input().split())
print('1'*(L-1)+'0' if N == 0 else '1'*(L-1)+str(N))