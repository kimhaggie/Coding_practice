#1261
import sys
from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def search(N,M,i,j,m,visit,step,next_target):
    #0인 것들 찾아다니기 
    #ans는 부셔야하는 벽들
    target = [[i,j]]
    visit[i][j]=True
    while len(target)!=0:
        cur_i,cur_j = target.pop()
        if cur_i==N-1 and cur_j==M-1:#찾음
            print(step)
            sys.exit()
        for idx in range(4):
            next_i = cur_i+dy[idx]
            next_j = cur_j+dx[idx]
            if 0<=next_i<N and 0<=next_j<M and (not visit[next_i][next_j]):
                if m[next_i][next_j]==-1:
                    if not [next_i,next_j] in next_target:
                        next_target.append([next_i,next_j])
                if m[next_i][next_j]==0:
                    visit[next_i][next_j]=True
                    target.append([next_i,next_j])

M, N = map(int,sys.stdin.readline().rstrip('\n').split(' '))
m = []
for _ in range(N):
    m.append(list(sys.stdin.readline().rstrip('\n')))
visit = [[False for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if m[i][j] == '0':
            m[i][j] = 0
        else:
            m[i][j] = -1
step = 0
target = [[0,0]]
while True:
    next_target = []
    for i,j in target:
        if not visit[i][j]:
            search(N,M,i,j,m,visit,step,next_target)
    for i,j in next_target:
        m[i][j] = 0
    target = next_target
    step+=1