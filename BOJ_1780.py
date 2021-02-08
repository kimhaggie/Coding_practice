#1780
import sys
from collections import deque
import math
import copy
import heapq

def check(m):
    size = len(m)
    cur = m[0][0]
    for i in range(size):
        for j in range(size):
            if m[i][j]!=cur:
                return False
    return True

def divide(m):
    size = len(m)
    if check(m):
        ans[m[0][0]+1] += 1
    else:
        new_size = int(size / 3)
        if size==3:
            for i in range(3):
                for j in range(3):
                    ans[m[i][j]+1] += 1
            return 0
        for i in range(3):
            for j in range(3):
                new_m = []
                for k in range(new_size):
                    new_m.append(m[i*new_size+k][j*new_size:(j+1)*new_size])
                divide(new_m)

N = int(sys.stdin.readline().rstrip('\n'))
m = []
for i in range(N):
    x = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
    m.append(x)
ans = [0,0,0]
divide(m)
print('\n'.join(map(str,ans)))