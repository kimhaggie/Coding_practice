#1080
import sys
from collections import deque
import math
import copy

def change(i,j):
    for x in range(i,i+3):
        for y in range(j,j+3):
            if A[x][y] == 1:
                A[x][y] = 0
            else:
                A[x][y] = 1 

N, M = map(int,sys.stdin.readline().rstrip('\n').split(' '))
A = []
B = []
for _ in range(N):
    x = sys.stdin.readline().rstrip('\n')
    tmp = []
    for val in x:
        tmp.append(int(val))
    A.append(tmp)
for _ in range(N):
    x = sys.stdin.readline().rstrip('\n')
    tmp = []
    for val in x:
        tmp.append(int(val))
    B.append(tmp)
ans = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            change(i,j)
            ans += 1
if A==B:
    print(ans)
else:
    print(-1)