N = int(input())
M = int(input())
K = int(input())
if N >= M and N >= K:
    print(N)
elif M >= N and M >= K:
    print(M)
else:
    print(K)
