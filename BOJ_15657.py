#15657
import sys
import math

def  func(a,i,n,m):
    ans = []
    if m==1:
        return [[a[k]] for k in range(i,n)]
    else:
        for k in range(i,n):
            for x in func(a,k,n,m-1):
                tmp = [a[k]]
                tmp.extend(x)
                ans.append(tmp)
    return ans

n,m = map(int,sys.stdin.readline().rstrip('\n').split(' '))
a = sys.stdin.readline().rstrip('\n').split(' ')
for idx,val in enumerate(a):
    a[idx]=int(val)
a.sort()
ans = func(a,0,n,m)
for x in ans:
    sys.stdout.write(' '.join(map(str,x))+'\n')