#1107
import sys
import math

def lower(a,length,n_s):
    if length==0:
        return [True,[]]
    low = []
    cur = int(n_s[0])
    poss = []#내림차순
    for j in a:
        if cur >= j:
            poss.append(j)
    for j in poss:
        if j==cur:
            low.append(j)
            result,sub_low = lower(a,length-1,n_s[1:])
            if result:
                low.extend(sub_low)
                return[True,low]
            else:
                del low[-1]
                continue
        else:
            low.append(j)
            while len(low)!=length:
                low.append(max(a))
            return [True,low]
    return [False,0]

def upper(a,length,n_s):
    if length==0:
        return [True,[]]
    up = []
    cur = int(n_s[0])
    poss = [] #오름차순
    for j in a:
        if cur <= j:
            poss.append(j)
    for j in poss:
        if j==cur:
            up.append(j)
            result,sub_up = upper(a,length-1,n_s[1:])
            if result:
                up.extend(sub_up)
                return [True,up]
            else:
                del up[-1]
                continue
        else:
            up.append(j)
            while len(up)!=length:
                up.append(min(a))
            return [True,up]
    return [False,0]

n = int(sys.stdin.readline().rstrip('\n'))
m = int(sys.stdin.readline().rstrip('\n'))
if m>0:
    a = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
    b = []
    for i in range(10):
        if i in a:
            continue
        else:
            b.append(i)
    a = b
else:
    a = list(range(10))
ans = []
ans.append(abs(n-100)) #현재 채널에서 +,-만 사용
length = len(str(n))
U = str(pow(10,length))
L = str(pow(10,length-1)-1)
n_s = str(n)
find = False
back=-1
up1 = upper(a,length,n_s)
up2 = upper(a,length+1,U)
low1 = lower(a[::-1],length,n_s)
if L!='0':
    low2 = lower(a[::-1],length-1,L)
else:
    if 0 in a:
        low2 =[True,[0]]
    else:
        low2 = [False,0]
for poss, val in [up1,up2,low1,low2]:
    if poss:
        cur = int(''.join(map(str,val)))
        tmp = len(str(cur))+abs(n-cur)
        ans.append(tmp)
    else:
        continue
if m!=10:
    print(min(ans))
else:
    print(abs(n-100))