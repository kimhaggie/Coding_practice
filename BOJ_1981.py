#1981
import sys
from collections import deque
import math
import copy
import heapq

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def BFS(l,u):
    visit = [[False for _ in range(n)] for _ in range(n)]
    visit[0][0] = True
    target = [[0,0]]
    if not l<=m[0][0]<=u or not l<=m[n-1][n-1]<=u:
        return False
    while target:
        new_target = []
        while target:
            cur = target.pop()
            if cur[0]==n-1 and cur[1]==n-1:
                return True
            for idx in range(4):
                next_i = cur[0]+dy[idx]
                next_j = cur[1]+dx[idx]
                if 0<=next_i<n and 0<=next_j<n and not visit[next_i][next_j] and l<=m[next_i][next_j]<=u:
                    new_target.append([next_i,next_j])
                    visit[next_i][next_j] = True
        target = new_target
    return False

def all(x):
    start = min_val
    end = start+x
    while end<=max_val:
        if BFS(start,end):
            return True
        start+=1
        end+=1
    return False

n = int(sys.stdin.readline().rstrip('\n'))
m = []
min_val = float('inf')
max_val = 0
for _ in range(n):
    x = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
    if min(x)<min_val:
        min_val = min(x)
    if max_val<max(x):
        max_val = max(x)
    m.append(x)
left = 0
right = max_val-min_val
mid = (left+right)//2
dp = [-1 for _ in range(201)]
while True:
    if dp[mid]==-1:
        dp[mid] = all(mid)
    if dp[mid-1]==-1:
        dp[mid-1] = all(mid-1)
    if dp[mid] and not dp[mid-1]:
        print(mid)
        break
    if dp[mid]:
        right = mid-1
    else:
        left = mid+1
    mid = (left+right)//2