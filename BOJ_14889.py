#14889
import sys

def func(start,m,S):
    if m == 0:
        sum1 = 0
        sum2 = 0
        remain = list(range(N))
        for i in ans:
            remain.remove(i)
        for i in range(int(N/2)):
            for j in range(int(N/2)):
                sum1 += S[ans[i]][ans[j]]
                sum2 += S[remain[i]][remain[j]]
        if x[0] > abs(sum1-sum2):
            x[0] = abs(sum1-sum2)
    else:
        for idx in range(start,len(S)):
            ans.append(idx)
            func(idx+1,m-1,S)
            ans.pop()

N = int(sys.stdin.readline().rstrip('\n'))
S = []
for _ in range(N):
    S.append(list(map(int,sys.stdin.readline().rstrip('\n').split())))
p = list(range(N))
ans = []
x = [float('inf')]
func(0,int(N/2),S)
print(x[0])