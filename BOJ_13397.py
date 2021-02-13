#13397
import sys
from collections import deque
import math
import copy
import heapq

def cal(a,k):
    return max(abs(min(a)-k),abs(max(a)-k))

def func(val):
    result = [[]for _ in range(M)]
    visit = [False for _ in range(N)]
    save = 0
    idx = 0
    while save<M:
        for i in range(idx,N):
            if not result[save]:
                result[save].append(A[i])
                visit[i] = True
            else:
                if cal(result[save],A[i])<=val:
                    result[save].append(A[i])
                    visit[i] = True
                else:
                    break
        idx = i
        save+=1
    return visit[-1]

N, M = map(int,sys.stdin.readline().rstrip('\n').split(' '))
A = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
left = 1
right = max(A)-min(A)
mid = (left+right)//2
while True:
    x = func(mid)
    if x and mid==0:
        print(mid)
        break
    if x and not func(mid-1):
        print(mid)
        break
    if x:
        right=mid-1
    else:
        left=mid+1
    mid=(left+right)//2