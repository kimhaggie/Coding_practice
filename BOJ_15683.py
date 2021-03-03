#15683
import sys
from collections import deque
import math
import copy
import heapq
from itertools import combinations

def right(i,j,m):
    while True:
        if not (0<=i<N and 0<=j<M) or m[i][j]=='6':
            break
        if m[i][j]=='0':
            m[i][j]='#'
        j+=1

def up(i,j,m):
    while True:
        if not (0<=i<N and 0<=j<M) or m[i][j]=='6':
            break
        if m[i][j]=='0':
            m[i][j]='#'
        i-=1

def left(i,j,m):
    while True:
        if not (0<=i<N and 0<=j<M) or m[i][j]=='6':
            break
        if m[i][j]=='0':
            m[i][j]='#'
        j-=1

def down(i,j,m):
    while True:
        if not (0<=i<N and 0<=j<M) or m[i][j]=='6':
            break
        if m[i][j]=='0':
            m[i][j]='#'
        i+=1

Ans = float('inf')

def compute(case):
    new_m = copy.deepcopy(m)
    for cam, pos, way in zip(num, cctv, case):
        i,j = pos
        if cam == 1:
            if way==0:
                right(i,j,new_m)
            elif way==1:
                up(i,j,new_m)
            elif way==2:
                left(i,j,new_m)
            elif way==3:
                down(i,j,new_m)
        elif cam == 2:
            way = way%2
            if way == 0:
                right(i,j,new_m)
                left(i,j,new_m)
            elif way == 1:
                up(i,j,new_m)
                down(i,j,new_m)
        elif cam == 3:
            if way==0:
                right(i,j,new_m)
                up(i,j,new_m)
            elif way==1:
                up(i,j,new_m)
                left(i,j,new_m)
            elif way==2:
                left(i,j,new_m)
                down(i,j,new_m)
            elif way==3:
                down(i,j,new_m)
                right(i,j,new_m)
        elif cam == 4:
            if way==0:
                right(i,j,new_m)
                up(i,j,new_m)
                left(i,j,new_m)
            elif way==1:
                up(i,j,new_m)
                left(i,j,new_m)
                down(i,j,new_m)
            elif way==2:
                left(i,j,new_m)
                down(i,j,new_m)
                right(i,j,new_m)
            elif way==3:
                down(i,j,new_m)
                right(i,j,new_m)
                up(i,j,new_m)
    ans = 0
    for i in range(N):
        for j in range(M):
            if new_m[i][j]=='0':
                ans+=1
    return ans

def DFS(cnt,n,path):
    if cnt==n:
        global Ans
        Ans = min(Ans,compute(path))
    else:
        for idx in range(4):
            path.append(idx)
            DFS(cnt+1,n,path)
            path.pop()


N, M = map(int,sys.stdin.readline().rstrip('\n').split(' '))
m = []
cctv = []
five = []
num = []
for i in range(N):
    line = list(sys.stdin.readline().rstrip('\n').split(' '))
    x = list(map(int,line))
    for j in range(M):
        if 0<x[j]<5:
            cctv.append([i,j])
            num.append(x[j])
        elif x[j]==5:
            five.append([i,j])
    m.append(line)
for i,j in five:#5번 카메라만 미리
    right(i,j,m)
    up(i,j,m)
    left(i,j,m)
    down(i,j,m)
'''
방향
0 오른쪽
1 위
2 왼쪽
3 아래
'''
path = []
DFS(0,len(cctv),path)
print(Ans)