#3055
import sys
from collections import deque
import math
import copy

dy = [-1,1,0,0]
dx = [0,0,1,-1]

def spread(m, water):
    new_m = copy.deepcopy(m)
    target = water
    new_water = []
    while target:
        cur = target.pop()
        for idx in range(4):
            next_i = cur[0]+dy[idx]
            next_j = cur[1]+dx[idx]
            if 0<=next_i<R and 0<=next_j<C and new_m[next_i][next_j] == '.':
                new_m[next_i][next_j] = '*'
                new_water.append([next_i,next_j])
    return [new_m, new_water]

def BFS(start,m):
    water = []
    for i in range(R):
        for j in range(C):
            if m[i][j] == '*':
                water.append([i,j])
    target = [start]
    step = 0
    while target:
        new_target = []
        new_m, new_water = spread(m,water)
        while target:
            cur = target.pop()
            for idx in range(4):
                next_i = cur[0]+dy[idx]
                next_j = cur[1]+dx[idx]
                if 0<=next_i<R and 0<=next_j<C and not visit[next_i][next_j]:
                    if m[next_i][next_j] == 'D':
                        print(step+1)
                        sys.exit()
                    if m[next_i][next_j] == '.' and new_m[next_i][next_j] == '.':
                        new_target.append([next_i,next_j])
                        visit[next_i][next_j] = True
        target = new_target
        m = new_m
        water = new_water
        step += 1
    print('KAKTUS')
    sys.exit()


R, C = map(int,sys.stdin.readline().rstrip('\n').split(' '))
m = []
start = []
visit = [[False for _ in range(C)] for _ in range(R)]
for i in range(R):
    x = list(sys.stdin.readline().rstrip('\n'))
    for j, val in enumerate(x):
        if val == 'S':
            x[j] = '.'
            start = [i,j]
            visit[i][j] = True
    m.append(x)
BFS(start,m)