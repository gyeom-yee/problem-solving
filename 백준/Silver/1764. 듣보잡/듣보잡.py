N, M, *A = open(0).read().split(); N=int(N)
subset = sorted(set(A[:N]) & set(A[N:]))
print(len(subset))
print("\n".join(subset))