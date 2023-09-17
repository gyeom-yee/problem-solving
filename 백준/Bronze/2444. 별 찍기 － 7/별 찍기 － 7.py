n = int(input())
j = 0
for i in range(1, 2*n):
    if i > n:
        j += 2
    print(" " * (n-(i-j)) + "*" * (2*(i-j)-1))