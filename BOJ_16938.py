#16938
import sys
from collections import deque
import math
import copy
import heapq
from itertools import combinations as C

N, L, R, X = map(int,sys.stdin.readline().rstrip('\n').split(' '))
A = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
#bitmask 32768
ans = 0
for case in range(1<<N):
    target = []
    for idx in range(N):
        if 1<<idx & case:
            target.append(A[idx])
    if len(target) < 2:
        continue
    if not L<=sum(target)<=R:
        continue
    if max(target)-min(target)>=X:
        ans+=1
print(ans)