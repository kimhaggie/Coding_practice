#15654
import sys
import math

def  func(a,i,m):
    ans = []
    if m==1:
        return [[a[k]] for k in range(len(a))]
    else:
        for k in range(i,len(a)):
            b=a.copy()
            del b[k]
            for x in func(b,0,m-1):
                tmp = [a[k]]
                tmp.extend(x)
                ans.append(tmp)
    return ans

n,m = map(int,sys.stdin.readline().rstrip('\n').split(' '))
a = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
a.sort()
ans = func(a,0,m)
for x in ans:
    print(' '.join(map(str,x)))