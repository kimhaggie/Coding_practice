#1202
import sys
from collections import deque
import math
import copy
import heapq

N, K = map(int,sys.stdin.readline().rstrip('\n').split(' '))
P = []
for _ in range(N):
    P.append(list(map(int,sys.stdin.readline().rstrip('\n').split(' '))))
C = []
for _ in range(K):
    C.append(int(sys.stdin.readline().rstrip('\n')))
P = sorted(P)
C = sorted(C)
h = []
k = 0
ans = 0
for idx in range(K):
    while k<N and P[k][0]<=C[idx]:
        heapq.heappush(h, [-P[k][1],P[k][1]])
        k += 1
    if h:
        ans += heapq.heappop(h)[1]
print(ans)