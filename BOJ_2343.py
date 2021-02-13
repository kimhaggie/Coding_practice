#2343
import sys
from collections import deque
import math
import copy
import heapq

def func(val):
    result = [[] for _ in range(M)]
    visit = [False for _ in range(N)]
    save = 0
    idx = 0
    while save < M:
        cur = 0
        for i in range(idx,len(A)):
            if cur+A[i]<=val:
                cur+=A[i]
                visit[i]=True
            else:
                idx = i
                break
        result[save] = cur
        save+=1
    if visit[-1]:
        return True
    else:
        return False

N, M = map(int,sys.stdin.readline().rstrip('\n').split(' '))
A = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
left = min(A)
right = sum(A)
mid = (left+right)//2
while True:
    x = func(mid)
    if x and not func(mid-1):
        print(mid)
        break
    if x:
        right = mid-1
    else:
        left = mid+1
    mid = (left+right)//2