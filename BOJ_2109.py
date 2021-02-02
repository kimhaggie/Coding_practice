#2109
import sys
from collections import deque
import math
import copy
import heapq

n = int(sys.stdin.readline().rstrip('\n'))
p = []
for _ in range(n):
    x = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
    p.append(x)
p = sorted(p, key = lambda x:x[1])
index = len(p) - 1
h = []
ans = 0
for x in reversed(range(1,10001)):
    if index == -1:#더이상 p가 없음
        if h:
            ans += heapq.heappop(h)[1]
            continue
        else:
            break
    if index>=0 and p[index][1] != x:
        if h:
            ans += heapq.heappop(h)[1]
        continue
    cur = p[index]
    while cur[1] == x:
        heapq.heappush(h,[-cur[0],cur[0]])
        index -= 1
        if index<0:
            break
        else:
            cur = p[index]
    if h:
        ans += heapq.heappop(h)[1]
print(ans)