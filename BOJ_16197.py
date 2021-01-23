#16197
import sys
from collections import deque
import math

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def  move(direction,ball1,ball2,m):
    N=len(m)
    M=len(m[0])
    if direction==0:#오른쪽
        y1,x1 = ball1[0],ball1[1]+1
        y2,x2 = ball2[0],ball2[1]+1
        flag1=False
        flag2=False
        
        if not(0<=y1<N and 0<=x1<M):
            flag1=True
        elif m[y1][x1]=='#':
            x1 = ball1[1]
        elif m[y1][x1]=='.':
            pass
        if not(0<=y2<N and 0<=x2<M):
            flag2=True
        elif m[y2][x2]=='#':
            x2 = ball2[1]
        elif m[y2][x2]=='.':
            pass
        return [flag1,flag2,[[y1,x1],[y2,x2]]]
    if direction==1:#왼쪽
        y1,x1 = ball1[0],ball1[1]-1
        y2,x2 = ball2[0],ball2[1]-1
        flag1=False
        flag2=False
        
        if not(0<=y1<N and 0<=x1<M):
            flag1=True
        elif m[y1][x1]=='#':
            x1 = ball1[1]
        elif m[y1][x1]=='.':
            pass
        if not(0<=y2<N and 0<=x2<M):
            flag2=True
        elif m[y2][x2]=='#':
            x2 = ball2[1]
        elif m[y2][x2]=='.':
            pass
        return [flag1,flag2,[[y1,x1],[y2,x2]]]
    if direction==2:#위쪽
        y1,x1 = ball1[0]-1,ball1[1]
        y2,x2 = ball2[0]-1,ball2[1]
        flag1=False
        flag2=False
        
        if not(0<=y1<N and 0<=x1<M):
            flag1=True
        elif m[y1][x1]=='#':
            y1 = ball1[0]
        elif m[y1][x1]=='.':
            pass
        if not(0<=y2<N and 0<=x2<M):
            flag2=True
        elif m[y2][x2]=='#':
            y2 = ball2[0]
        elif m[y2][x2]=='.':
            pass
        return [flag1,flag2,[[y1,x1],[y2,x2]]]
    if direction==3:#아래쪽
        y1,x1 = ball1[0]+1,ball1[1]
        y2,x2 = ball2[0]+1,ball2[1]
        flag1=False
        flag2=False
        
        if not(0<=y1<N and 0<=x1<M):
            flag1=True
        elif m[y1][x1]=='#':
            y1 = ball1[0]
        elif m[y1][x1]=='.':
            pass
        if not(0<=y2<N and 0<=x2<M):
            flag2=True
        elif m[y2][x2]=='#':
            y2 = ball2[0]
        elif m[y2][x2]=='.':
            pass
        return [flag1,flag2,[[y1,x1],[y2,x2]]]

def BFS(ball1,ball2,m):
    target = [[ball1,ball2]]
    step = 1
    while target:
        if step==11:
            print(-1)
            sys.exit()
        new_target = []
        while target:
            cur = target.pop()
            cur1 = cur[0]
            cur2 = cur[1]
            for idx in range(4):
                result = move(idx,cur1,cur2,m)
                if (result[0] and not result[1]) or (not result[0] and result[1]):
                    print(step)
                    sys.exit()
                if result[2][0]!=result[2][1] and not result[0] and not result[1]:
                    if not result[2] in new_target:
                        new_target.append(result[2])
        target = new_target
        step+=1

N,M = map(int,sys.stdin.readline().rstrip('\n').split(' '))
m = []
for _ in range(N):
    m.append(list(sys.stdin.readline().rstrip('\n')))
ball1 = []
ball2 = []
for i in range(N):
    for j in range(M):
        if m[i][j] == 'o':
            if len(ball1)==0:
                ball1 = [i,j]
            else:
                ball2 = [i,j]
BFS(ball1,ball2,m)