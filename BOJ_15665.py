#15665
import sys
import math

def func(a,i,c):
    if c==m:
        if ''.join(map(str,ans)) not in total:
            print(*ans)
            total.add(''.join(map(str,ans)))
        return
    for j in range(i,n):
        ans.append(a[j])
        func(a,0,c+1)
        ans.pop()

n,m = map(int,sys.stdin.readline().rstrip('\n').split(' '))
a = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
a.sort()
total = set()
ans=[]
func(a,0,0)