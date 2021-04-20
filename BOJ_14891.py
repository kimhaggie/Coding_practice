import sys
from collections import deque

def clock(x):
    x.appendleft(x.pop())
    return x

def reverse_clock(x):
    x.append(x.popleft())
    return x

gear = []

def check(l,r):
    return gear[l][2]!=gear[r][6]

for i in range(4):
    x = list(sys.stdin.readline().rstrip('\n'))
    x = list(map(int,x))
    gear.append(deque(x))
K = int(sys.stdin.readline().rstrip('\n'))
cmd = []
for i in range(K):
    cmd.append(list(map(int,sys.stdin.readline().rstrip('\n').split())))
    cmd[-1][0]-=1
for g, d in cmd:
    target = [[g,d]]
    visit = [False for _ in range(4)]
    visit[g] = True
    while target:
        cur_g, cur_d = target.pop()
        if cur_g==0:
            if check(cur_g,cur_g+1) and not visit[cur_g+1]:
                if cur_d==-1:
                    next_d=1
                else:
                    next_d=-1
                target.append([cur_g+1,next_d])
                visit[cur_g+1] = True
        elif cur_g==3:
            if check(cur_g-1,cur_g) and not visit[cur_g-1]:
                if cur_d==-1:
                    next_d=1
                else:
                    next_d=-1
                target.append([cur_g-1,next_d])
                visit[cur_g-1] = True
        else:
            if cur_d==-1:
                next_d=1
            else:
                next_d=-1
            if check(cur_g,cur_g+1) and not visit[cur_g+1]:
                target.append([cur_g+1,next_d])
                visit[cur_g+1] = True
            if check(cur_g-1,cur_g) and not visit[cur_g-1]:
                target.append([cur_g-1,next_d])
                visit[cur_g-1] = True
        if cur_d==1:
            gear[cur_g] = clock(gear[cur_g])
        elif cur_d==-1:
            gear[cur_g] = reverse_clock(gear[cur_g])
ans = 0
for i in range(4):
    if gear[i][0]==1:
        ans+=pow(2,i)
print(ans)