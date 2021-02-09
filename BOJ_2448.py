#2448
import sys
from collections import deque
import math
import copy
import heapq

def func(i,j,n):
    if n==3:
        m[i][j+2]='*'
        m[i+1][j+1]='*'
        m[i+1][j+3]='*'
        for x in range(j,j+5):
            m[i+2][x]='*'
    else:
        func(i,j+n//2,n//2)
        func(i+n//2,j,n//2)
        func(i+n//2,j+2*n//2,n//2)
        
n = int(sys.stdin.readline().rstrip('\n'))
m = [[' ' for _ in range(2*n-1)] for i in range(n)]
func(0,0,n)
for x in m:
    print(*x,sep='')