#14889
import sys

def bitcount(b):
    if b==0:
        return 0
    else:
        return b%2 + bitcount(b//2) 

N = int(sys.stdin.readline().rstrip('\n'))
S = []
for _ in range(N):
    S.append(list(map(int,sys.stdin.readline().rstrip('\n').split(' '))))
n = 1<<N
ans = float('inf')
for B in range(n):
    if bitcount(B) == N//2:
        tmp1 = 0
        tmp2 = 0
        for i in range(N):
            for j in range(i+1,N):
                if (1<<i)&B > 0 and (1<<j)&B > 0:
                    tmp1 += S[i][j]
                    tmp1 += S[j][i]
                if (1<<i)&~B > 0 and (1<<j)&~B > 0:
                    tmp2 += S[i][j]
                    tmp2 += S[j][i]
        if abs(tmp1-tmp2) < ans:
            ans = abs(tmp1-tmp2)
print(ans)