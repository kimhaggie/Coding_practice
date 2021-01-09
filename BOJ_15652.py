#15652
import sys
import math

def  func(i,j,m):
    ans = []
    if m==1:
        return [[k] for k in range(i,j+1)]
    else:
        for k in range(i,j+1):
            for x in func(k,j,m-1):
                tmp = [k]
                tmp.extend(x)
                ans.append(tmp)
    return ans

n,m = map(int,sys.stdin.readline().rstrip('\n').split(' '))
ans = func(1,n,m)
for x in ans:
    print(' '.join(map(str,x)))