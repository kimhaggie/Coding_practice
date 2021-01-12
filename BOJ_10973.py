#10973
import sys

def func(a):
    sort = True
    for idx in range(1,len(a)):
        if a[idx-1] > a[idx]:
            sort = False
            break
    if sort:
        return -1
    target = -1
    for idx in range(1,len(a)):
        if a[idx-1] < a[idx]:
            target = idx - 1
            break
    if target == -1:
        a[-1],a[-2]=a[-2],a[-1]
        return a
    x = -1
    for idx in reversed(range(target,len(a))):
        if a[idx-1] > a[idx]:
            x = idx-1
            break
    max_val = 0
    max_idx = -1
    for idx in range(x+1,len(a)):
        if max_val<a[idx]<a[x]:
            max_val = a[idx]
            max_idx = idx
    a[max_idx],a[x] = a[x],a[max_idx]
    a[x+1:]=sorted(a[x+1:],reverse=True)
    return a

n = int(sys.stdin.readline().rstrip('\n'))
a = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
ans = func(a)
if ans==-1:
    print(-1)
else:
    print(' '.join(map(str,ans)))