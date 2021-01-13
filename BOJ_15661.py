#15661
import sys

def func(start,m,S):
    if m == 0:
        sum1 = 0
        sum2 = 0
        remain = list(range(N))
        for i in ans:
            remain.remove(i)
        l1 = len(ans)
        for i in range(l1):
            for j in range(l1):
                sum1 += S[ans[i]][ans[j]]
        
        for i in range(len(S)-l1):
            for j in range(len(S)-l1):
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
for i in range(2,int(N/2)+1):
    func(0,i,S)
print(x[0])