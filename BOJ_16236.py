#16236
import sys
from collections import deque
import math
import copy

dy = [-1,1,0,0]
dx = [0,0,1,-1]

def find(m,start,size):
    visit = [[False for _ in range(N)] for _ in range(N)]
    visit[start[0]][start[1]] = True
    target = [start] #i,j
    flag = False
    ans = []
    step = 1
    while target:
        new_target = []
        while target:
            cur = target.pop()
            for idx in range(4):
                next_i = cur[0]+dy[idx]
                next_j = cur[1]+dx[idx]
                if 0<=next_i<N and 0<=next_j<N and not visit[next_i][next_j]:
                    if m[next_i][next_j] == size or m[next_i][next_j] == 0:
                        new_target.append([next_i,next_j])
                        visit[next_i][next_j] = True
                    elif m[next_i][next_j] < size:
                        flag = True
                        ans.append([next_i,next_j])
                        visit[next_i][next_j] = True
            pass
        target = new_target
        step += 1
        if flag:
            break
    min_i = 20
    tmp = []
    for i,j in ans:
        if i < min_i:
            min_i = i
            tmp = [i,j]
        elif i == min_i:
            if j<tmp[1]:
                tmp = [i,j]
    return [flag,tmp,step-1]

def BFS(start):
    cur = start
    size = 2
    cnt = 0
    d = 0
    while True:
        flag,goal,step=find(m,cur,size)
        if not flag:#먹을 게 없다.
            print(d)
            sys.exit()
        m[goal[0]][goal[1]] = 0
        cnt += 1
        cur = goal
        d += step
        if cnt==size:
            size+=1
            cnt=0

N = int(sys.stdin.readline().rstrip('\n'))
m = []
start = []
for i in range(N):
    x = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
    for j, val in enumerate(x):
        if val == 9:
            x[j] = 0
            start = [i,j]
    m.append(x)
BFS(start)