import sys
import copy

def clock(point, center):
    y,x = point
    c2,c1 = center
    return [c2-(c1-x), c1+(c2-y)]

N = int(sys.stdin.readline().rstrip('\n'))
cmd = []
for _ in range(N):
    cmd.append(list(map(int,sys.stdin.readline().rstrip('\n').split())))
dragon_0 = [[[0,0],[0,1]]]
for idx in range(1,11):
    prev = dragon_0[idx-1]
    center = prev[-1]
    tmp = copy.deepcopy(prev)
    for point in reversed(prev[:-1]):
        tmp.append(clock(point,center))
    dragon_0.append(tmp)
dragon_1=[]#위
dragon_2=[]#왼쪽
dragon_3=[]#아래
for d in dragon_0:
    a = copy.deepcopy(d)
    for idx in range(len(d)):
        a[idx] = clock(a[idx],[0,0])
    dragon_3.append(a)
    b = copy.deepcopy(a)
    for idx in range(len(d)):
        b[idx] = clock(b[idx],[0,0])
    dragon_2.append(b)
    c = copy.deepcopy(b)
    for idx in range(len(d)):
        c[idx] = clock(c[idx],[0,0])
    dragon_1.append(c)
m = [[0 for _ in range(101)]for _ in range(101)]
for c in cmd:
    x,y,d,g = c
    cur = []
    if d==0:
        cur = dragon_0[g]
    elif d==1:
        cur = dragon_1[g]
    elif d==2:
        cur = dragon_2[g]
    else:
        cur = dragon_3[g]
    for i,j in cur:
        if 0<=i+y<=100 and 0<=j+x<=100:
            m[i+y][j+x]=1
ans=0
for i in range(100):
    for j in range(100):
        if m[i][j]==1 and m[i+1][j]==1 and m[i][j+1]==1 and m[i+1][j+1]==1:
            ans+=1
print(ans)