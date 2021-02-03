#1783
import sys
from collections import deque
import math
import copy
import heapq

dy = [-2,-1,1,2]
dx = [1,2,2,1]

def DFS(i,j,depth):
    if depth==3:
        return depth
    ans = depth
    for idx in range(4):
        next_i = i+dy[idx]
        next_j = j+dx[idx]
        if 0<=next_i<N and 0<=next_j<M:
            ans=max(ans,DFS(next_i,next_j,depth+1))
    return ans

N, M = map(int,sys.stdin.readline().rstrip('\n').split(' '))
#4번까지 이동
ans=DFS(N-1,0,0)+1
if N>=3 and M>=7:
    #위아래
    cur = [N-1,6]
    ans=max(ans,4+M-7+1)
print(ans)