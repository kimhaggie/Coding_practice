#1339
import sys
from collections import deque

def func(total,alpha,line,m,n,d,visit):
    if m == n:
        #print(d)
        ans = 0
        for idx, val in enumerate(total):
            tmp = 0
            for x in val:
                tmp+=d[x]
            ans+= pow(10,7-idx)*tmp
        return ans
    else:
        ans = 0
        for val in range(10-len(alpha),10):
            if not visit[val]:
                d[alpha[m]]=val
                visit[val] = True
                tmp = func(total,alpha,line,m+1,n,d,visit)
                if ans < tmp:
                    ans = tmp
                visit[val]=False
    return ans

N = int(sys.stdin.readline().rstrip('\n'))
line = []
alpha = set()
for _ in range(N):
    x = list(sys.stdin.readline().rstrip())
    line.append(x)
    for val in x:
        alpha.add(val)
alpha=list(alpha)
visit = [False for _ in range(10)]
d = dict()
total = [[] for _ in range(8)]
for x in line:
    for idx,val in enumerate(reversed(x)):
        total[7-idx].append(val)
print(func(total,alpha,line,0,len(alpha),d,visit))