#1300
import sys
from collections import deque
import math
import copy
import heapq

def check(val):
    ans = 0
    for i in range(1,N+1):
        ans+=min(val//i,N)
    return ans

N = int(sys.stdin.readline().rstrip('\n'))
k = int(sys.stdin.readline().rstrip('\n'))

left = 1
right = N*N
mid = (left+right)//2
while True:
    x = check(mid)
    if check(mid-1)<k<=x:
        print(mid)
        break
    if x<k:
        left = mid+1
    else:
        right = mid-1
    mid = (left+right)//2