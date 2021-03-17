#17070
import sys
from collections import deque
import math
import copy
import heapq
from itertools import combinations

ans = 0

def DFS(i,j,x):
    global ans
    if i==N-1 and j==N-1:
        ans+=1
        return 0
    if x==1 or x==3:#가로가 될 수 있는 경우
        if j+1 < N and m[i][j+1]==0:
            DFS(i,j+1,1)
    if x==2 or x==3:#세로가 될 수 있는 경우
        if i+1 < N and m[i+1][j]==0:
            DFS(i+1,j,2)
    if x==1 or x==2 or x==3:#대각선이 될 수 있는 경우
        if i+1 < N and j+1 < N and (m[i][j+1]==0 and m[i+1][j]==0 and m[i+1][j+1]==0):
            DFS(i+1,j+1,3)

N = int(sys.stdin.readline().rstrip('\n'))
m = []
for i in range(N):
    x = list(map(int,sys.stdin.readline().rstrip('\n').split()))
    m.append(x)
DFS(0,1,1)
print(ans)