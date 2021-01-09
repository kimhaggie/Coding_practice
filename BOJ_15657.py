#15657
import sys
import math

def func(i,c):
    if c==m:
        print(*ans)
        return
    for j in range(i,n):
        ans.append(a[j])
        func(j,c+1)
        ans.pop()

n,m = map(int,sys.stdin.readline().rstrip('\n').split(' '))
a = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
a.sort()
ans=[]
func(0,0)