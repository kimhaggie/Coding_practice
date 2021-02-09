#11729
import sys
from collections import deque
import math
import copy
import heapq

def move(n,start,end):
    if n==1:
        print(start, end)
    else:
        rest = 6-start-end
        move(n-1,start,rest)
        print(start, end)
        move(n-1,rest,end)

N = int(sys.stdin.readline().rstrip('\n'))
print(pow(2,N)-1)
move(N,1,3)