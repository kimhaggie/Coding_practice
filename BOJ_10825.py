#10825
import sys
from collections import deque
import math
import copy
import heapq

N = int(sys.stdin.readline().rstrip('\n'))
A = []
for _ in range(N):
    x = list(sys.stdin.readline().rstrip('\n').split(' '))
    x[1]=int(x[1])
    x[2]=int(x[2])
    x[3]=int(x[3])
    A.append(x)
A=sorted(A,key=lambda x:x[0])
A=sorted(A,key=lambda x:x[3],reverse=True)
A=sorted(A,key=lambda x:x[2])
A=sorted(A,key=lambda x:x[1],reverse=True)
for val in A:
    print(val[0])