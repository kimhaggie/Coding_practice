#1744
import sys
from collections import deque
import math
import copy
import heapq

N = int(sys.stdin.readline().rstrip('\n'))
plus=[]
minus=[]
for _ in range(N):
    x = int(sys.stdin.readline().rstrip('\n'))
    if x>0:
        heapq.heappush(plus,[-x,x])
    else:
        heapq.heappush(minus,x)
ans = 0
while len(plus)>1:
    a = heapq.heappop(plus)[1]
    b = heapq.heappop(plus)[1]
    if a==1 or b==1:
        ans+=a
        ans+=b
    else:
        ans+=a*b
if plus:
    ans+=plus[0][1]
while len(minus)>1:
    a = heapq.heappop(minus)
    b = heapq.heappop(minus)
    ans+=a*b
if minus:
    ans+=minus[0]
print(ans)