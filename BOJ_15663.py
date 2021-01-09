#15663
import sys
import math

def func(a,i,c,l):
    if c==m:
        if ''.join(map(str,ans)) not in total:
            print(*ans)
            total.add(''.join(map(str,ans)))
        return
    for j in range(i,l):
        b=a.copy()
        b.remove(a[j])
        ans.append(a[j])
        func(b,0,c+1,l-1)
        ans.pop()

n,m = map(int,sys.stdin.readline().rstrip('\n').split(' '))
a = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
a.sort()
total = set()
ans=[]
func(a,0,0,len(a))