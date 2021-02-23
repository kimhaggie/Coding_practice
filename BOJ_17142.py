#17142
import sys
from collections import deque
import math
import copy
import heapq
from itertools import combinations

def com(x):
    ans = []
    target = [[]]
    while target:
        cur = target.pop()
        if len(cur)==0:
            for i in range(x):
                tmp = cur.copy()
                tmp.append(i)
                target.append(tmp)
        elif len(cur)!=M:
            if cur[-1]==x-1:
                continue
            for i in range(cur[-1]+1,x):
                tmp = cur.copy()
                tmp.append(i)
                target.append(tmp)
        else:
            ans.append(cur)
    return ans

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def BFS(case):
    target = []
    for idx in case:
        target.append(virus[idx])
    visit = [[-1 for _ in range(N)] for _ in range(N)]
    for val in target:
        visit[val[0]][val[1]]=0
    step = 0
    while target:
        step += 1
        new_target = []
        while target:
            cur = target.pop()
            for idx in range(4):
                next_i=cur[0]+dy[idx]
                next_j=cur[1]+dx[idx]
                if 0<=next_i<N and 0<=next_j<N and (m[next_i][next_j]=='0' or m[next_i][next_j]=='2') and visit[next_i][next_j]==-1:
                    visit[next_i][next_j]=step
                    new_target.append([next_i,next_j])
        target = new_target
    flag = True
    ans = -1
    for i in range(N):
        for j in range(N):
            if visit[i][j]!=-1:
                if m[i][j]!='2':
                    ans = max(ans,visit[i][j])
                else:
                    tmp = False
                    for idx in range(4):
                        next_i = i+dy[idx]
                        next_j = j+dx[idx]
                        if 0<=next_i<N and 0<=next_j<N and m[i][j]=='0':
                            tmp = True
                    if tmp:
                        ans = max(ans,visit[i][j]-1)
            if m[i][j]=='0' and visit[i][j]==-1:
                flag = False
                break
        if not flag:
            break
    return flag, ans

N, M = map(int,sys.stdin.readline().rstrip('\n').split(' '))
m = []
virus = []
for i in range(N):
    x = sys.stdin.readline().rstrip('\n').split(' ')
    for j in range(N):
        if x[j]=='2':
            virus.append([i,j])
    m.append(x)
ans = float('inf')
for case in com(len(virus)):
    result = BFS(case)
    if result[0]:
        ans = min(ans,result[1])
if ans == float('inf'):
    print(-1)
else:
    if ans==-1:
        print(0)
    else:
        print(ans)