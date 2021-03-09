#17089
import sys
from collections import deque
import math
import copy
import heapq
from itertools import combinations

def compute(path):
    ans = 0
    for val in path:
        ans += len(friend[val])-2
    return ans

ans = float('inf')

def DFS(path):
    global ans
    if len(path)==3:
        return compute(path)
    prev = -1
    if path:
        prev = path[-1]
    for idx in range(prev+1, N):
        flag = True
        for x in path:
            if not idx in friend[x]:
                flag = False
        if flag:
            path.append(idx)
            x = DFS(path)
            if x != None and ans >= x:
                ans = x
            path.pop()

N, M = map(int,sys.stdin.readline().rstrip('\n').split())
friend = [set() for _ in range(N)]
for _ in range(M):
    a, b = map(int,sys.stdin.readline().rstrip('\n').split())
    a -= 1
    b -= 1
    friend[a].add(b)
    friend[b].add(a)
DFS([])
if ans == float('inf'):
    print(-1)
else:
    print(ans)