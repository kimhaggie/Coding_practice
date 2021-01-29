#6087
import sys
from collections import deque
import math
import copy

dy = [-1,1,0,0]
dx = [0,0,-1,1]
#상하좌우

def BFS():
    target = [start]
    while target:
        new_target = []
        while target:
            cur = target.pop()
            for idx in range(4):
                next_i = cur[0]+dy[idx]
                next_j = cur[1]+dx[idx]
                if 0<=next_i<H and 0<=next_j<W and m[next_i][next_j] != '*':
                    if cur[2]==-1:#이제 출발
                        visit[next_i][next_j][idx] = 0
                        if m[next_i][next_j] != 'C':
                            new_target.append([next_i,next_j,idx])
                    else:
                        if idx == cur[2]:#같은 방향
                            if visit[next_i][next_j][idx]==-1 or visit[cur[0]][cur[1]][idx] < visit[next_i][next_j][idx]:
                                visit[next_i][next_j][idx] = visit[cur[0]][cur[1]][idx]
                                if m[next_i][next_j] != 'C':
                                    new_target.append([next_i,next_j,idx])
                        else:#다른 방향
                            if visit[next_i][next_j][idx]==-1 or visit[cur[0]][cur[1]][cur[2]]+1 < visit[next_i][next_j][idx]:
                                visit[next_i][next_j][idx] = visit[cur[0]][cur[1]][cur[2]]+1
                                if m[next_i][next_j] != 'C':
                                    new_target.append([next_i,next_j,idx])
        target = new_target
    x = visit[goal[0]][goal[1]]
    tmp = []
    for val in x:
        if val!=-1:
            tmp.append(val)
    print(min(tmp))

W, H = map(int,sys.stdin.readline().rstrip('\n').split(' '))
m = []
flag = False
C = []
for i in range(H):
    x = list(sys.stdin.readline().rstrip('\n'))
    for j in range(W):
        if x[j]=='C':
            C.append([i,j,-1])
    m.append(x)
start=C[0]
goal=C[1]
visit= [[[-1, -1, -1, -1] for _ in range(W)] for _ in range(H)]
visit[start[0]][start[1]] = [0,0,0,0]
BFS()