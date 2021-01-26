#14502
import sys
from collections import deque
import math
import copy

dy = [1,-1,0,0]
dx = [0,0,1,-1]

def cal(m,virus):
    target = []
    for val in virus:
        target.append(val)
    while target:
        new_target = []
        while target:
            cur = target.pop()
            for idx in range(4):
                next_i = cur[0] + dy[idx]
                next_j = cur[1] + dx[idx]
                if 0<=next_i<N and 0<=next_j<M and m[next_i][next_j]==0:
                    m[next_i][next_j] = 2
                    new_target.append([next_i,next_j])
        target = new_target
    ans = 0
    for i in range(N):
        for j in range(M):
            if m[i][j]==0:
                ans+=1
    return ans


def DFS(start,m,empty,step,virus):
    if step == 3:
        x = cal(copy.deepcopy(m),virus)
        return x
    n = len(empty)
    ans = 0
    for i in range(start,n):
        cur = empty[i]
        m[cur[0]][cur[1]] = 1
        x = DFS(i+1,m,empty,step+1,virus)
        if ans < x:
            ans = x
        m[cur[0]][cur[1]] = 0
    return ans

N, M = map(int,sys.stdin.readline().rstrip('\n').split(' '))
m = []
visit = [[False for _ in range(M)] for _ in range(N)]
empty = []
virus = []
for i in range(N):
    x = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
    m.append(x)
    for j,val in enumerate(x):
        if val == 0:
            empty.append([i,j])
        if val == 2:
            virus.append([i,j])
print(DFS(0,m,empty,0,virus))