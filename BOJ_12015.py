#12015
import sys
from collections import deque
import math
import copy
import heapq

def search(A,val):
    left = 0
    right = len(A) - 1
    mid = (left + right) // 2
    if mid <= 1:
        for idx, x in enumerate(A):
            if val <= x:
                return idx
    while True:
        if A[mid] == val:
            return mid
        elif A[mid] < val:
            left = mid
            mid = (left + right) // 2
            if A[mid] < val <= A[mid+1]:
                return mid+1
        else:#val < A[mid]
            right = mid
            mid = (left + right) // 2
            if A[mid-1] < val <= A[mid]:
                return mid        

N = int(sys.stdin.readline().rstrip('\n'))
A = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
v = [0]
for x in A:
    if v[-1] < x:
        v.append(x)
        continue
    idx = search(v, x)
    v[idx] = x
print(len(v)-1)