#10026
import sys
from collections import deque
import math
import copy

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def spread(m,i,j,val,visit):
    target = [[i,j]]
    color = m[i][j]
    visit[i][j] = val
    while target:
        new_target = []
        while target:
            cur = target.pop()
            for idx in range(4):
                next_i = cur[0]+dy[idx]
                next_j = cur[1]+dx[idx]
                if 0<=next_i<N and 0<=next_j<N and m[next_i][next_j]==color and visit[next_i][next_j]==0:
                    visit[next_i][next_j] = val
                    new_target.append([next_i,next_j])
        target = new_target

def BFS(m):
    visit = [[0 for _ in range(N)] for _ in range(N)]
    step = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j]==0:
                step+=1
                spread(m,i,j,step,visit)
    return step

N = int(sys.stdin.readline().rstrip('\n'))
m = []
M = []
for _ in range(N):
    x = list(sys.stdin.readline().rstrip('\n'))
    m.append(x)
    y = x.copy()
    for j,val in enumerate(y):
        if val == 'G':
            y[j] = 'R'
    M.append(y)
print(BFS(m),end=' ')
print(BFS(M))