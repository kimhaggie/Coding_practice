#1561
import sys
from collections import deque
import math
import copy
import heapq

def state(val):
    ans = 0
    S = []
    for x in A:
        ans+=val//x+1
        S.append(val%x)
    return ans,S

def step(n,S):
    for idx,val in enumerate(A):
        S[idx]=(S[idx]+1)%val
    remain = N-n
    target = []
    for idx,val in enumerate(S):
        if val==0:
            target.append(idx+1)
    print(target[remain-1])

N, M = map(int,sys.stdin.readline().rstrip('\n').split(' '))
A = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
left = 0
right = N*min(A)
mid = (left+right)//2
while True:
    x = state(mid)
    if x[0]<N and state(mid+1)[0]>=N:
        step(x[0],x[1])
        break
    if x[0]<=N-1:
        left = mid+1
    if x[0]>N-1:
        right = mid-1
    mid = (left+right)//2