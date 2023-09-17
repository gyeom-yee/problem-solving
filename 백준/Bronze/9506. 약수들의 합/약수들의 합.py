import sys
for x in sys.stdin:
    n = int(x)
    if n == -1: break
    arr = []
    for i in range(1,n+1):
        if n%i == 0 and n != i:
            arr.append(i)
    if sum(arr) != n:
        print(f"{n} is NOT perfect.")
    else:
        print(n,"=", end=" ")
        print(*arr, sep=" + ")