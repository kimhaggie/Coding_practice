#2422
import sys
from collections import deque
import math
import copy
import heapq
from itertools import combinations

ans = 0

def DFS(path):
    global ans
    if len(path)==3:
        ans+=1
    else:
        prev = -1
        if path:
            prev = path[-1]
        for i in range(prev+1,N):
            flag = True
            for j in avoid[i]:
                if j in path:
                    flag = False
            if not flag:
                continue
            path.append(i)
            DFS(path)
            path.pop()

N, M = map(int,sys.stdin.readline().rstrip('\n').split())
avoid = [set() for _ in range(N)]
for _ in range(M):
    x, y = map(int,sys.stdin.readline().rstrip('\n').split())
    x-=1
    y-=1
    avoid[x].add(y)
    avoid[y].add(x)
path = []
DFS(path)
print(ans)