#1939
import sys
from collections import deque
import math
import copy
import heapq

def bfs(val):
    V = set()
    E = [set() for _ in range(N+1)]
    for a,b,c in zip(A,B,C):
        if c >= val:
            E[a].add(b)
            E[b].add(a)
            V.add(a)
            V.add(b)
    for idx,val in enumerate(E):
        E[idx] = list(val)
    V = list(V)
    target = [plant[0]]
    visit = [False for _ in range(N+1)]
    visit[plant[0]] = True
    while target:
        new_target = []
        while target:
            cur = target.pop()
            if cur == plant[1]:
                return True
            for x in E[cur]:
                if not visit[x]:
                    new_target.append(x)
                    visit[x] = True
        target = new_target
    return False

N, M = map(int,sys.stdin.readline().rstrip('\n').split(' '))
A, B, C = [], [], []
for _ in range(M):
    x = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
    A.append(x[0])
    B.append(x[1])
    C.append(x[2])
plant = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
left = 1
right = max(C)
mid = (left+right)//2
while True:
    x = bfs(mid)
    if x and not bfs(mid+1):
        print(mid)
        break
    if x:
        left = mid+1
        mid = (left+right)//2
        continue
    else:
        right = mid-1
        mid = (left+right)//2
        continue