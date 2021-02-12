#1654
import sys
from collections import deque
import math
import copy
import heapq

def count(A,val):
    ans = 0
    for x in A:
        ans+=(x//val)
    return ans

K, N =map(int,sys.stdin.readline().rstrip('\n').split(' '))
A = []
for _ in range(K):
    A.append(int(sys.stdin.readline().rstrip('\n')))
left = 1
right = max(A)
mid = (left+right)//2
while True:
    if count(A,mid)>=N and count(A,mid+1)<N:
        print(mid)
        sys.exit()
    if count(A,mid)>=N:#더 크게 잘라도 됨
        left = mid+1
        mid = (left+right)//2 
        continue
    if count(A,mid)<=N:#더 작게 잘라야 함
        right = mid-1
        mid = (left+right)//2
        continue