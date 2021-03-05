#2210
import sys
from collections import deque
import math
import copy
import heapq
from itertools import combinations

dy = [-1,1,0,0]
dx = [0,0,-1,1]

ans = set()
def DFS(i,j,path):
    global ans
    if len(path)==6:
        ans.add(''.join(path))
    else:
        for idx in range(4):
            next_i = i+dy[idx]
            next_j = j+dx[idx]
            if 0<=next_i<5 and 0<=next_j<5:
                path.append(m[next_i][next_j])
                DFS(next_i,next_j,path)
                path.pop()

m = []
for _ in range(5):
    m.append(sys.stdin.readline().rstrip('\n').split())
for i in range(5):
    for j in range(5):
        path = [m[i][j]]
        DFS(i,j,path)
print(len(ans))