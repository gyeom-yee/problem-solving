N, B = map(int, input().split())
arr = []
while N//B !=0 :
    arr.append(chr(N%B+55) if N%B >= 10 else str(N % B))
    N //= B
arr.append(chr(N+55) if N >= 10 else str(N))
print("".join(reversed(arr)))