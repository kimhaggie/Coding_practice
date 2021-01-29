#16954
import sys
from collections import deque
import math
import copy

dy = [0,0,1,1,1,0,-1,-1,-1]
dx = [0,1,1,0,-1,-1,-1,0,1]

def move_map(m, wall):
    next_map = []
    next_wall = wall
    for val in m[-1]:
        if val == '#':
            next_wall -= 1
    next_map.append(['.' for _ in range(8)])
    for idx in range(7):
        next_map.append(m[idx])
    return [next_map, next_wall]

def BFS(m, wall):
    target = [[8-1,0]]
    wall = wall
    while target:
        new_target = []
        if wall==0:
            print(1)
            sys.exit()
        while target:
            cur = target.pop()
            new_m, new_wall = move_map(m,wall)
            for idx in range(9):
                next_i = cur[0]+dy[idx]
                next_j = cur[1]+dx[idx]
                if 0<=next_i<8 and 0<=next_j<8:
                    if m[next_i][next_j] == '.':
                        if new_m[next_i][next_j] == '.':
                            new_target.append([next_i,next_j])
        target = new_target
        m = new_m
        wall = new_wall
    print(0)
    sys.exit()

m = []
wall = 0
for _ in range(8):
    x = list(sys.stdin.readline().rstrip('\n'))
    m.append(x)
    for val in x:
        if val == '#':
            wall += 1
BFS(m, wall)