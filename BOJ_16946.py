#16946
import sys
from collections import deque
import math
import copy

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def zero(m,i,j,visit,x):
    t = [[i,j]]
    visit[i][j] = 1
    final = []
    step = 0
    while t:
        new_target = []
        while t:
            cur = t.pop()
            final.append(cur)
            step += 1
            for idx in range(4):
                next_i = cur[0]+dy[idx]
                next_j = cur[1]+dx[idx]
                if 0<=next_i<N and 0<=next_j<M and visit[next_i][next_j]==0 and m[next_i][next_j]=='0': 
                    visit[next_i][next_j] = 1
                    new_target.append([next_i,next_j])
        t = new_target
    for i,j in final:
        visit[i][j] = x
    X.append(step)   

def BFS(m):
    visit = [[0 for _ in range(M)] for _ in range(N)]
    target = wall
    num=1
    while target:
        cur = target.pop()
        tmp = 0
        egg=[]
        for idx in range(4):
            next_i = cur[0]+dy[idx]
            next_j = cur[1]+dx[idx]
            if 0<=next_i<N and 0<=next_j<M and m[next_i][next_j]=='0':
                if visit[next_i][next_j] == 0:
                    zero(m,next_i,next_j,visit,num)
                    num+=1
                    tmp += X[visit[next_i][next_j]]
                    egg.append(visit[next_i][next_j])
                else:
                    if not visit[next_i][next_j] in egg:    
                        tmp += X[visit[next_i][next_j]]
                        egg.append(visit[next_i][next_j])
        ans[cur[0]][cur[1]] = str((tmp+1)%10)


N, M = map(int,sys.stdin.readline().rstrip('\n').split(' '))
m = []
empty = []
wall = []
X=[None]
for i in range(N):
    x = sys.stdin.readline().rstrip('\n')
    m.append(list(x))
    for j in range(M):
        if x[j]=='0':
            empty.append([i,j])
        else:
            wall.append([i,j])
ans = copy.deepcopy(m)
BFS(m)
for val in ans:
    print(*val,sep='')