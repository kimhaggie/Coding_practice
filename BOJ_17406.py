#17406
import sys
from collections import deque
import math
import copy
import heapq
from itertools import combinations

def rotate_clock(r,c,s):
    r -= 1
    c -= 1
    for radius in range(1, s+1):
        A = []
        width = 2*radius+1
        cur_i, cur_j = r-radius, c-radius
        A.append(m[cur_i+1][cur_j])
        for x in range(width):
            A.append(m[cur_i][cur_j+x])
        for x in range(1, width):
            A.append(m[cur_i+x][cur_j+width-1])
        for x in range(1, width):
            A.append(m[cur_i+width-1][cur_j+width-x-1])
        for x in range(1, width-2):
            A.append(m[cur_i+width-x-1][cur_j])
        idx = 0
        for x in range(width):
            m[cur_i][cur_j+x] = A[idx]
            idx+=1
        for x in range(1, width):
            m[cur_i+x][cur_j+width-1] = A[idx]
            idx+=1
        for x in range(1, width):
            m[cur_i+width-1][cur_j+width-x-1] = A[idx]
            idx+=1
        for x in range(1, width-1):
            m[cur_i+width-x-1][cur_j] = A[idx]
            idx+=1

def rotate_reverse(r,c,s):
    r -= 1
    c -= 1
    for radius in range(1, s+1):
        A = []
        width = 2*radius+1
        cur_i, cur_j = r-radius, c-radius+1
        A.append(m[cur_i][cur_j])
        for x in range(1, width-1):
            A.append(m[cur_i][cur_j+x])
        for x in range(1, width):
            A.append(m[cur_i+x][cur_j+width-2])
        for x in range(1, width):
            A.append(m[cur_i+width-1][cur_j+width-x-2])
        for x in range(width-1):
            A.append(m[cur_i+width-x-2][cur_j-1])
            
        cur_i, cur_j = r-radius, c-radius
        idx = 0
        for x in range(width):
            m[cur_i][cur_j+x] = A[idx]
            idx+=1
        for x in range(1, width):
            m[cur_i+x][cur_j+width-1] = A[idx]
            idx+=1
        for x in range(1, width):
            m[cur_i+width-1][cur_j+width-x-1] = A[idx]
            idx+=1
        for x in range(1, width-1):
            m[cur_i+width-x-1][cur_j] = A[idx]
            idx+=1

def compute(path):
    ans = float('inf')
    for idx in path:
        r,c,s = map(int,cmd[idx])
        rotate_clock(r,c,s)

    for x in m:
        tmp = sum(list(map(int,x)))
        ans = min(tmp,ans)

    for idx in reversed(path):
        r,c,s = map(int,cmd[idx])
        rotate_reverse(r,c,s)

    return ans

def DFS(path):
    if len(path) == K:
        return compute(path)
    ans = float('inf')
    for idx in range(K):
        if idx in path:
            continue
        path.append(idx)
        x = DFS(path)
        ans = min(ans,x)
        path.pop()
    return ans
    

N, M, K = map(int,sys.stdin.readline().rstrip('\n').split())
m = []
for i in range(N):
    x = sys.stdin.readline().rstrip('\n').split()
    m.append(x)
cmd = []
for i in range(K):
    x = sys.stdin.readline().rstrip('\n').split()
    cmd.append(x)
ans = DFS([])
print(ans)