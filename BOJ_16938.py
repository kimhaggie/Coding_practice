#16936
import sys
from collections import deque
import math
import copy
import heapq
from itertools import combinations as C

H, W = map(int,sys.stdin.readline().rstrip('\n').split(' '))
N = int(sys.stdin.readline().rstrip('\n'))
S = []
for _ in range(N):
    S.append(list(map(int,sys.stdin.readline().rstrip('\n').split(' '))))
ans = 0
for i in range(N-1):
    for j in range(i+1,N):
        x = S[i]
        y = S[j]
        flag = False
        h = H-x[0]
        w = W-x[1]
        if h>=0 and w>=0:
            #case1 0 0
            if (y[0]<=h and y[1]<=W) or (y[0]<=H and y[1]<=w):
                flag = True
            #case2 0 90
            if (y[1]<=h and y[0]<=W) or (y[1]<=H and y[0]<=w):
                flag = True
        h = H-x[1]
        w = W-x[0]
        if h>=0 and w>=0:
            #case3 90 0
            if (y[0]<=h and y[1]<=W) or (y[0]<=H and y[1]<=w):
                flag = True
            #case4 90 90
            if (y[1]<=h and y[0]<=W) or (y[1]<=H and y[0]<=w):
                flag = True
        if flag:
            ans = max(ans,x[0]*x[1]+y[0]*y[1])
print(ans)