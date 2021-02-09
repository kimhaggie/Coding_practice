#2447
import sys
from collections import deque
import math
import copy
import heapq

def func(i,j,n):
    if n==3:
        for x in range(j,j+3):
            m[i][x]='*'
        for x in range(j,j+3,2):
            m[i+1][x]='*'
        for x in range(j,j+3):
            m[i+2][x]='*'
    else:
        for x in range(3):
            for y in range(3):
                if x==1 and y==1:
                    continue
                func(i+x*n//3,j+y*n//3,n//3)

n = int(sys.stdin.readline().rstrip('\n'))
m = [[' ' for _ in range(n)] for _ in range(n)]
func(0,0,n)
for x in m:
    print(*x,sep='')