#1074
import sys
from collections import deque
import math
import copy
import heapq

def find(n,i,j):
    if n==2:
        if i==0 and j==0:
            return 1
        elif i==0 and j==1:
            return 2
        elif i==1 and j==0:
            return 3
        else:
            return 4
    if i<n/2 and j<n/2:
        return find(n/2,i,j)
    elif i<n/2 and j>=n/2:
        return (n/2)*(n/2)+find(n/2,i,j-n/2)
    elif i>=n/2 and j<n/2:
        return (n/2)*(n/2)*2+find(n/2,i-n/2,j)
    else:
        return (n/2)*(n/2)*3+find(n/2,i-n/2,j-n/2)

N, r, c = map(int,sys.stdin.readline().rstrip('\n').split(' '))
n = pow(2,N)
print(int(find(n,r,c)-1))