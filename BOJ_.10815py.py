#10815
import sys
from collections import deque
import math
import copy
import heapq

def search(val):
    left = 0
    right = N-1
    mid = int((left+right)/2)
    while left<=right:
        if C[mid] == val:
            return 1
        if C[mid] < val:
            left = mid + 1
            mid = int((left + right)/2)
        else:
            right = mid - 1
            mid = int((left + right)/2)
    return 0

N = int(sys.stdin.readline().rstrip('\n'))
C = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
M = int(sys.stdin.readline().rstrip('\n'))
I = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
C.sort()
for val in I:
    print(search(val),end = ' ')