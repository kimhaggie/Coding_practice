#10972
import sys

def func(a,start):
    target = -1
    for idx in range(start,len(a)-1):
        if a[idx]>a[idx+1]:
            target = idx
            break
    if target == -1:
        a[-2],a[-1]=a[-1],a[-2]
        return a
    reverse = True
    for idx in range(target,len(a)-1):
        if a[idx]<a[idx+1]:
            reverse = False
    if reverse:
        if target==0:
            return -1
        min_idx = -1
        min_val = 10001
        for idx in range(target,len(a)):
            if a[target-1]<a[idx] and a[idx]<min_val:
                min_val = a[idx]
                min_idx = idx
        a[min_idx],a[target-1] = a[target-1],a[min_idx]
        a[target:] = sorted(a[target:])
    else:
        for idx in reversed(range(target+1,len(a))):
            if a[idx-1] < a[idx]:
                x = idx
                break
        a = func(a,x)
    return a

n = int(sys.stdin.readline().rstrip('\n'))
a = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
if n==1:
    print(-1)
else:
    ans = func(a,0)
    if ans == -1:
        print(-1)
    else:
        print(' '.join(map(str,ans)))