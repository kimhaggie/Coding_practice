#10974
import sys

def func(a,m):
    if m==1:
        ans.append(a[0])
        print(' '.join(ans))
        ans.pop()
    for idx,val in enumerate(a):
        ans.append(a[idx])
        b = a.copy()
        b.remove(val)
        func(b,m-1)
        ans.pop()

n = int(sys.stdin.readline().rstrip('\n'))
a= list(map(str,range(1,n+1)))
ans = []
func(a,len(a))