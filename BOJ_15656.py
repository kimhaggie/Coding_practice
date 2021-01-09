#15656
import sys
import math

def  func(a,n,m):
    ans = []
    if m==1:
        return [[a[k]] for k in range(n)]
    else:
        for k in range(n):
            for x in func(a,n,m-1):
                tmp = [a[k]]
                tmp.extend(x)
                ans.append(tmp)
    return ans

n,m = map(int,sys.stdin.readline().rstrip('\n').split(' '))
a = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
a.sort()
ans = func(a,n,m)
for x in ans:
    sys.stdout.write(' '.join(map(str,x))+'\n')