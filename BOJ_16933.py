#16933
import sys
from collections import deque
import math
import copy

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def BFS():
    target = [[0,0,0]]
    visit[0][0][0]=True
    step = 0
    while target:
        new_target = []
        step += 1#step이 홀수면 낮 짝수면 밤
        while target:
            cur = target.pop()
            if cur[0]==N-1 and cur[1]==M-1:
                print(step)
                sys.exit()
            wall = False
            for idx in range(4):
                next_i = cur[0]+dy[idx]
                next_j = cur[1]+dx[idx]
                if 0<=next_i<N and 0<=next_j<M:
                    if step%2==0:#밤일 때
                        if m[next_i][next_j] == '0' and not visit[next_i][next_j][cur[2]]:
                            visit[next_i][next_j][cur[2]] = True
                            new_target.append([next_i,next_j,cur[2]])
                        if m[next_i][next_j] == '1' and cur[2]<K and not visit[next_i][next_j][cur[2]+1]:
                            wall = True
                    else:#낮일 때
                        if m[next_i][next_j] == '0' and not visit[next_i][next_j][cur[2]]:
                            visit[next_i][next_j][cur[2]] = True
                            new_target.append([next_i,next_j,cur[2]])
                        if m[next_i][next_j] == '1' and cur[2]<K and not visit[next_i][next_j][cur[2]+1]:
                            visit[next_i][next_j][cur[2]+1] = True
                            new_target.append([next_i,next_j,cur[2]+1])
            if wall and step%2==0:
                new_target.append(cur)
        target = new_target
    print(-1)

N, M, K = map(int,sys.stdin.readline().rstrip('\n').split(' '))
m = []
visit = [[[False for _ in range(K+1)] for _ in range(M)] for _ in range(N)]
for i in range(N):
    x = list(sys.stdin.readline().rstrip('\n'))
    m.append(x)
BFS()