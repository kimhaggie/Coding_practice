#15649
import sys
import math

def f(a,m):
    ans = []
    if m==1:
        return [[k] for k in a]
    else:
        for k in a:
            b=a.copy()
            b.remove(k)
            for x in f(b,m-1):
                tmp = [k]
                tmp.extend(x)
                ans.append(tmp)
    return ans 

n,m = map(int,sys.stdin.readline().rstrip('\n').split(' '))
ans = f([i for i in range(1,n+1)],m)
for x in ans:
    print(' '.join(map(str,x)))