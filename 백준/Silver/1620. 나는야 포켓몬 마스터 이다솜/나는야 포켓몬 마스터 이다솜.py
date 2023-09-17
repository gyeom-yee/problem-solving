N, M, *A = open(0).read().split();N=int(N)
k = {v:str(i+1) for i,v in enumerate(A[:N])}
print("\n".join(A[int(i)-1] if i.isnumeric() else k[i] for i in A[N:]))