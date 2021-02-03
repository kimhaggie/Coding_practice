#12970
import sys
from collections import deque
import math
import copy
import heapq

N, K = map(int,sys.stdin.readline().rstrip('\n').split(' '))
idx = 1
ans = []
while idx<N:
    if K  <= idx*(N-idx):
        break
    idx+=1
if idx==N:
    print(-1)
    sys.exit()
B = N-idx
pos = [0 for _ in range(idx+1)]
for x in reversed(range(idx+1)):
    for k in reversed(range(B+1)):
        if x*k<=K:
            pos[x]=k
            K-=x*k
            B-=k
            break
ans = ''
for x in pos:
    for i in range(x):
        ans+='B'
    ans+='A'
print(ans[:-1])            