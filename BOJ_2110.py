#2110
import sys
from collections import deque
import math
import copy
import heapq

def check(A,val):
    c = C - 1
    prev = A[0]
    for x in A: 
        if x-prev>=val:
            c-=1
            prev =x
    if c<=0:
        return True
    else:
        return False

N, C = map(int,sys.stdin.readline().rstrip('\n').split())
A = []
for _ in range(N):
    A.append(int(sys.stdin.readline().rstrip('\n')))
A.sort()
left = 1
right = A[-1]-A[0]
mid = (left+right)//2
while True:
    x = check(A,mid)
    if x and not check(A,mid+1):
        print(mid)
        break
    if x:
        left=mid+1
        mid=(left+right)//2
        continue
    if not x:
        right=mid-1
        mid=(left+right)//2
        continue