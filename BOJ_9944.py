#9944
import sys
from collections import deque
import math
import copy
import heapq
from itertools import combinations

dy = [-1,1,0,0]
dx = [0,0,1,-1]
#위 아래 오른쪽 왼쪽

def go(i,j,way):
    cnt = 0
    while True:
        next_i = i+dy[way]
        next_j = j+dx[way]
        if not (0<=next_i<N and 0<=next_j<M):
            break
        if m[next_i][next_j] == '*':
            break
        cnt+=1
        m[next_i][next_j] = '*'
        i = next_i
        j = next_j
    return cnt,i,j

def back(i,j,way,cnt):
    while cnt != 0:
        m[i][j]='.'
        i = i-dy[way]
        j = j-dx[way]
        cnt-=1

def DFS(i,j,depth,cnt):
    ans = float('inf')
    if depth == 1000000:
        return float('inf')
    if cnt == 0:
        return depth
    for idx in range(4):
        next_i = i+dy[idx]
        next_j = j+dx[idx] 
        if (0<=next_i<N and 0<=next_j<M) and m[next_i][next_j] == '.':
            tmp,tmp_i,tmp_j = go(i,j,idx)
            x = DFS(tmp_i,tmp_j,depth+1,cnt-tmp)
            ans = min(x,ans)
            back(tmp_i,tmp_j,idx,tmp)
    return ans
idx = 1
while True:
    cmd = sys.stdin.readline().rstrip('\n')
    ans = float('inf')
    if not cmd:
        break
    N, M = map(int,cmd.split())
    m = []
    total = 0
    for i in range(N):
        x = list(sys.stdin.readline().rstrip('\n'))
        for j in range(M):
            if x[j]=='.':
                total+=1
        m.append(x)
    for i in range(N):
        for j in range(M):
            if m[i][j]=='.':
                m[i][j]='*'
                x = DFS(i,j,0,total-1)
                ans = min(x,ans)
                m[i][j]='.'
    print('Case ',idx,':',sep='',end=' ')
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)
    idx+=1