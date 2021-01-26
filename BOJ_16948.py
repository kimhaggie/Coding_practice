#16948
import sys
from collections import deque
import math

dy = [-2,-2,0,0,2,2,]
dx = [-1,1,-2,2,-1,1]

def BFS(N,visit,p1,p2):
    step = 0
    target = [p1]
    while target:
        new_target = []
        while target:
            cur = target.pop()
            if cur==p2:
                print(step)
                sys.exit()
            for idx in range(6):
                next_i = cur[0]+dy[idx]
                next_j = cur[1]+dx[idx]
                if 0<=next_i<N and 0<=next_j<N and not visit[next_i][next_j]:
                    new_target.append([next_i,next_j])
                    visit[next_i][next_j] = True
        target = new_target
        step += 1
    print(-1)

N = int(sys.stdin.readline().rstrip('\n'))
r1,c1,r2,c2 = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
p1 = [r1,c1]
p2 = [r2,c2]
visit = [[False for _ in range(N)] for _ in range(N)]
visit[r1][c1] = True
BFS(N, visit, p1, p2)