#2580
import sys
from collections import deque
import math

def DFS(n,N,empty,m):
    if n == 0:
        for idx in range(9):
            print(*m[idx])
        sys.exit(0)
    cur = empty[N-n]
    a = list(range(1,10))
    block_i = cur[0]//3
    block_j = cur[1]//3
    for y in range(block_i*3,block_i*3+3):
        for x in range(block_j*3,block_j*3+3):
            if m[y][x] in a:
                a.remove(m[y][x])
    for x in range(9):
        if m[cur[0]][x] in a:
            a.remove(m[cur[0]][x])
        if m[x][cur[1]] in a:
            a.remove(m[x][cur[1]])

    for val in a:
        m[cur[0]][cur[1]]=val
        DFS(n-1,N,empty,m)
        m[cur[0]][cur[1]]=0

m = []
empty = []
for idx in range(9):
    x=list(map(int,sys.stdin.readline().rstrip('\n').split()))
    m.append(x)
    for k in range(9):
        if x[k]==0:
            empty.append([idx,k])
n = len(empty)
DFS(n,n,empty,m)