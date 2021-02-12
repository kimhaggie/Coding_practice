#2022
import sys
from collections import deque
import math
import copy
import heapq

def equation(k):
    return (c/math.sqrt(x*x-k*k))+(c/math.sqrt(y*y-k*k))-1

x, y, c = map(float,sys.stdin.readline().rstrip('\n').split(' '))
if x < y:#x가 항상 큼
    x, y = y, x
left = 0.0
right = y
mid = (left+right)/2
prev = mid
while True:
    result = equation(mid)
    if result > 0:
        right = mid+0.0001
        mid = (left+right)/2
    else:
        left = mid+0.0001
        mid = (left+right)/2
    if abs(prev-mid)<0.0001:
        print('%.3f'%(mid))
        break
    prev = mid