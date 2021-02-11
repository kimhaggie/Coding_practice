#2261
import sys
from collections import deque
import math
import copy
import heapq

def distance(x,y):
    return (x[0]-y[0])*(x[0]-y[0])+(x[1]-y[1])*(x[1]-y[1])

def divide(pos):
    if len(pos)==1:
        return float('inf')
    if len(pos)==2:
        return distance(pos[0],pos[1])
    n = len(pos)
    mid_x = pos[n//2][0]
    dl = divide(pos[:n//2])
    dr = divide(pos[n//2:])
    d = min(dl,dr)
    lower = math.floor(mid_x-math.sqrt(d))
    upper = math.ceil(mid_x+math.sqrt(d))
    target = []
    for val in pos:
        if lower<=val[0]<=upper:
            target.append(val)
    target = sorted(target,key = lambda x:x[1],reverse = True)
    min_val = float('inf')
    while target:
        cur = target.pop()
        idx = len(target)-1
        while True:
            if idx<0:
                break
            tmp = target[idx]
            # if (cur[1]-tmp[1])*(cur[1]-tmp[1])>=d:
            #     break
            if abs(cur[1]-tmp[1])>=math.sqrt(d):
                break
            idx-=1
            tmp_distance = distance(cur,tmp)
            if tmp_distance<min_val:
                min_val=tmp_distance
    return min(d,min_val)

n = int(sys.stdin.readline().rstrip('\n'))
pos = []
for _ in range(n):
    pos.append(list(map(int,sys.stdin.readline().rstrip('\n').split(' '))))
pos.sort()
print(divide(pos))