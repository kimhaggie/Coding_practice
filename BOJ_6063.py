#6603
import sys

def func(a,start,mask,m,k):
    if m == 0:
        tmp = []
        for idx in range(k):
            if not mask[idx]:
                tmp.append(a[idx])
        if len(tmp)==6:
            print(' '.join(tmp))
    for idx in range(start,len(a)):
        if mask[idx]:
            mask[idx] = False
            func(a,idx+1,mask,m-1,k)
            mask[idx] = True
        
    

while(True):
    a = sys.stdin.readline().rstrip('\n')
    if a=='0':
        break
    a = a.split(' ')
    k = int(a[0])
    a = a[1:]
    mask = [True for _ in range(k)]
    func(a,0,mask,6,k)
    print()