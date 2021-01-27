#12866
import sys
from collections import deque
import math
import copy

def compute(l,i,j):
    x = l.copy()
    if x[i]<x[j]:
        x[j]-=x[i]
        x[i]*=2
    else:
        x[i]-=x[j]
        x[j]*=2
    return sorted(x)

def BFS(start):
    if start[0]==start[1]==start[2]:
        return 1
    if (start[0]+start[1]+start[2])%3!=0:
        return 0
    start = sorted(start)
    S = sum(start)
    target = [start]
    visit = [[False for _ in range(1000)] for _ in range(1000)]
    visit[start[0]][start[1]] = True
    while target:
        new_target = []
        while target:
            cur = target.pop()
            for i in range(3):
                for j in range(i+1,3):
                    if cur[i]!=cur[j]:
                        x=compute(cur,i,j)
                        if x[0]<=0 or x[1]<=0 or x[2]<=0:
                            continue
                        if x[0]==x[1]==S-x[0]-x[1]:
                            return 1
                        if not visit[x[0]][x[1]]:
                            visit[x[0]][x[1]] = True
                            new_target.append(x)
        target = new_target
    return 0

start = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
print(BFS(start))