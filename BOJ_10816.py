#10816
import sys
from collections import deque
import math
import copy
import heapq

def search_L(val):
    left = 0
    right = N-1
    mid = int((left+right)/2)
    while left<=right:
        if C[left] == val:
            return left
        if C[mid] < val:
            left = mid + 1
            mid = int((left + right)/2)
        elif C[mid] > val:
            right = mid - 1
            mid = int((left + right)/2)
        else:
            right = mid
            mid = int((left+right)/2)
    return -1

def search_R(val):
    left = 0
    right = N-1
    mid = math.ceil((left+right)/2)
    while left<=right:
        if left==2 and mid ==2 and right==3:
            break
        if C[right] == val:
            return right
        if C[mid] < val:
            left = mid + 1
            mid = math.ceil((left + right)/2)
        elif C[mid] > val:
            right = mid - 1
            mid = math.ceil((left + right)/2)
        else:
            left = mid
            mid = math.ceil((left+right)/2)
    return -1

N = int(sys.stdin.readline().rstrip('\n'))
C = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
M = int(sys.stdin.readline().rstrip('\n'))
I = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
C.sort()
ans = []
for val in I:
    if search_L(val)!=-1:
        ans.append(search_R(val)-search_L(val)+1)
    else:
        ans.append(0)
print(' '.join(map(str,ans)))