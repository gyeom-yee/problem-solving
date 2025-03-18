import sys
arr = list(map(int, sys.stdin.readlines()))
even_arr = [a for a in arr if a%2 != 0]
if even_arr:
    print(sum(even_arr))
    print(min(even_arr))
else:
    print(-1)