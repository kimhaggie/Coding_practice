#2805
import sys
from collections import deque
import math
import copy
import heapq

def count(A,val):
    ans = 0
    for x in A:
        cur = x-val
        if cur > 0:
            ans+=cur
    return ans

N, M = map(int,sys.stdin.readline().rstrip('\n').split(' '))
A = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
left = 0
right = max(A)
mid = (left+right)//2
while True:
    if count(A,mid)>=M and count(A,mid+1)<M:
        print(mid)
        sys.exit()
    if count(A,mid)>=M:
        left = mid+1
        mid = (left+right)//2
        continue
    if count(A,mid)<=M:
        right = mid-1
        mid = (left+right)//2
        continue