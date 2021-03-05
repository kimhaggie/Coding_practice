#15686
import sys
from collections import deque
import math
import copy
import heapq
from itertools import combinations

def diff(x,y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])

def compute(path):
    ans = [float('inf') for _ in range(len(house))]
    for i in path:
        for idx, j in enumerate(db[i]):
            if j < ans[idx]:
                ans[idx] = j
    return sum(ans)

Ans = float('inf')

def DFS(path):
    global Ans
    if len(path) == M:
        result = compute(path)
        if result < Ans:
            Ans = result
    else:
        prev = -1
        if path:
            prev = path[-1]
        for i in range(prev+1, num):
            path.append(i)
            DFS(path)
            path.pop()

N, M = map(int,sys.stdin.readline().rstrip('\n').split())
house = []
chicken = []
m = []
for i in range(N):
    x = list(map(int,sys.stdin.readline().rstrip('\n').split()))
    for j in range(N):
        if x[j] == 1:
            house.append([i,j])
        if x[j] == 2:
            chicken.append([i,j])
    m.append(x)
path = []
num = len(chicken)
db = []
for c in chicken:
    cur = []
    for h in house:
        cur.append(diff(c,h))
    db.append(cur)
DFS(path)
print(Ans)