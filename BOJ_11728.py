#11728
import sys
from collections import deque
import math
import copy
import heapq

N, M = map(int,sys.stdin.readline().rstrip('\n').split(' '))
A = sorted(list(map(int,sys.stdin.readline().rstrip('\n').split(' '))))
B = sorted(list(map(int,sys.stdin.readline().rstrip('\n').split(' '))))
C = []
i=0
j=0
while i<N and j<M:
    if A[i]<B[j]:
        C.append(A[i])
        i+=1
    else:
        C.append(B[j])
        j+=1
if A:
    C.extend(A[i:])
if B:
    C.extend(B[j:])
print(' '.join(map(str,C)))