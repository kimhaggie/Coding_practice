#16917
import sys
from collections import deque
import math
import copy
import heapq

A, B, C, X, Y = map(int,sys.stdin.readline().rstrip('\n').split(' '))
m = max(X,Y)*2 #반반 갯수
ans = float('inf')
for i in range(0,m+1,2):
    if X-i/2>=0 and Y-i/2>=0:
        ans = min(ans,i*C+(X-i/2)*A+(Y-i/2)*B)
    elif X-m/2<0:
        ans = min(ans,i*C+(Y-i/2)*B)
    else:
        ans = min(ans,i*C+(X-i/2)*A)
print(int(ans))