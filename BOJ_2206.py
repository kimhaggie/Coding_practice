#2206
import sys
from collections import deque
import math
import copy

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def BFS(m):
    target = [[0,0,False]] #i,j, 벽뚫기 사용여부
    step = 0
    visit = [[[False,False] for _ in range(M)] for _ in range(N)]#X,O
    visit[0][0][0] = True
    while target:
        step += 1
        new_target = []
        while target:
            cur = target.pop()
            if cur[0]==N-1 and cur[1]==M-1:
                return step
            for idx in range(4):
                next_i = cur[0] + dy[idx]
                next_j = cur[1] + dx[idx]
                if 0<=next_i<N and 0<=next_j<M:
                    if m[next_i][next_j]=='0':
                        if cur[2] and not visit[next_i][next_j][1]:
                            new_target.append([next_i,next_j,cur[2]])
                            visit[next_i][next_j][1] = True
                        if not cur[2] and not visit[next_i][next_j][0]:
                            new_target.append([next_i,next_j,cur[2]])
                            visit[next_i][next_j][0] = True
                    elif m[next_i][next_j]=='1':
                        if cur[2]:#더이상 벽뚫기 x
                            continue
                        else:
                            if not visit[next_i][next_j][1]:
                                new_target.append([next_i,next_j,True])
                                visit[next_i][next_j][1] = True
        target = new_target
    return -1

N, M = map(int,sys.stdin.readline().rstrip('\n').split(' '))
m = []
for _ in range(N):
    m.append(list(sys.stdin.readline().rstrip('\n')))
print(BFS(m))